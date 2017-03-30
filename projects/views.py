from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView, UpdateView
from django.core.files.storage import FileSystemStorage
from projects.models import InvestmentCompany, Innovation
from users.models import User, Innovator
from projects.investor_form import InvestorForm
from projects.forms import StartupStageForm, IdeationStage
from projects.commitment_form import CommitmentForm1, CommitmentForm2, CommitmentForm3
from projects.concepting_form import ConceptingForm1, ConceptingForm2, ConceptingForm3
from projects.validation_form import ValidationForm1, ValidationForm2, ValidationForm3
from projects.scaling_form import ScalingForm1, ScalingForm2, ScalingForm3
from projects.establishing_form import EstablishingForm1, EstablishingForm2, EstablishingForm3
from form_helpers import handle_uploads

# Create your views here.


class EditInvestmentCompany(FormView):
    form_class = InvestorForm
    template_name = 'projects/investor_profile_wizard.html'

    def form_valid(self, form):
        investor = form.save(commit=False)
        investor.save()

        return super(EditInvestmentCompany, self).form_valid(form)

    def form_invalid(self, form):
        return super(EditInvestmentCompany, self).form_invalid(form)


class ViewInvestmentCompany(TemplateView):
    template_name = 'projects/view-investor.html'
    model = InvestmentCompany

    def get_context_data(self, **kwargs):
        context = super(ViewInvestmentCompany, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        context['company'] = user
        return context


def select_startup_stage(request):
    form = StartupStageForm()
    if request.method == 'POST':
        form = StartupStageForm(request.POST)

        if form.is_valid():
            stage = form.cleaned_data['idea_stage']
            stage = int(stage)
            prof = form.save(commit=False)
            innov = Innovator.objects.get(email=request.user.email)
            prof.lead = innov
            prof.save()

            innov.has_created_entity = True
            innov.save()

            if stage == 1:
                # idea
                return HttpResponseRedirect(reverse("projects:ideation"))
            elif stage == 2:
                # idea something to show
                return HttpResponseRedirect(reverse("projects:commitment"))
            elif stage == 3:
                # target and direction
                return HttpResponseRedirect(reverse("projects:concepting"))
            elif stage == 4:
                # testing with actual users
                return HttpResponseRedirect(reverse("projects:validation"))
            elif stage == 5:
                # grow business
                return HttpResponseRedirect(reverse("projects:scaling"))
            elif stage == 6:
                # maintain growth
                return HttpResponseRedirect(reverse("projects:establishing"))

        else:
            form = StartupStageForm(request.POST)
            return render(request, 'projects/startup_stage.html', {'form': form})

    else:
        return render(request, 'projects/startup_stage.html', {'form': form})


def ideation(request):
    form = IdeationStage()
    if request.method == "POST":
        form = IdeationStage(request.POST, request.FILES)
        if form.is_valid():
            proj = Innovation.objects.get(lead__email=request.user.email)
            cleaned_data = form.cleaned_data
            print cleaned_data
            proj.name = cleaned_data.get('name')
            proj.description = cleaned_data.get('description')
            proj.sectors = cleaned_data.get('sectors')
            proj.other_sectors = cleaned_data.get('other_sectors')
            proj.logo = cleaned_data.get('logo')
            proj.challenge_faced = cleaned_data.get("challenge_faced")
            proj.challenge_to_solve = cleaned_data.get("challenge_to_solve")

            proj.stage = 1
            proj.save()
            return HttpResponseRedirect(reverse("projects:view-startup"))
        else:
            return render(request, "projects/idea_wizard.html", {'form': form})
    else:
        return render(request, "projects/idea_wizard.html", {'form': form})


def view_startup(request):
    innovation_profile = get_object_or_404(Innovation, lead=request.user.id)
    return render(request, 'projects/view_startup.html', {'project': innovation_profile})


class EditIdeationProfile(UpdateView):
    form_class = IdeationStage


def commitment_view(request):
    proj = Innovation.objects.get(lead__email=request.user.email)

    commitment_form_1 = CommitmentForm1(request.FILES, instance=proj)
    commitment_form_2 = CommitmentForm2(request.FILES, instance=proj)
    commitment_form_3 = CommitmentForm3(request.FILES, instance=proj)

    active_form = 'form_1'

    if request.method == 'POST':
        print request.POST
        proj = Innovation.objects.get(lead__email=request.user.email)
        commitment_form_1 = CommitmentForm1(request.POST, request.FILES, instance=proj)

        if 'commitment_form_1' in request.POST:
            commitment_form_1 = CommitmentForm1(request.POST, request.FILES)
            if commitment_form_1.is_valid():
                print 'form is valid'
                proj = Innovation.objects.get(lead__email=request.user.email)
                cleaned_data = commitment_form_1.cleaned_data
                proj.name = cleaned_data.get('name')
                proj.description = cleaned_data.get('description')
                proj.sectors = cleaned_data.get('sectors')
                proj.other_sectors = cleaned_data.get('other_sectors')
                proj.logo = cleaned_data.get('logo')
                proj.service_pic = cleaned_data.get('service_pic')
                proj.service_videos = cleaned_data.get('service_videos')
                proj.challenge_faced = cleaned_data.get("challenge_faced")
                proj.challenge_to_solve = cleaned_data.get("challenge_to_solve")
                proj.url = cleaned_data.get('url')

                proj.stage = 2
                proj.save()

                active_form = 'form_2'

                return render(request, 'projects/commitment.html', {
                    'active_form': active_form,
                    'form1': CommitmentForm1(instance=proj),
                    'form2': CommitmentForm2(instance=proj),
                    'form3': CommitmentForm3(instance=proj),
                    'project': proj
                })

            else:
                active_form = 'form_1'
                return render(request, 'projects/commitment.html', {
                    'active_form': active_form,
                    'form1': commitment_form_1,
                    'form2': CommitmentForm2(instance=proj),
                    'form3': CommitmentForm3(instance=proj),
                    'project': proj
                })

        elif 'commitment_form_2' in request.POST:
            proj = Innovation.objects.get(lead__email=request.user.email)
            form_2 = CommitmentForm2(request.POST, request.FILES, instance=proj)
            if form_2.is_valid():
                proj_form = form_2.save(commit=False)
                proj_form.save()

                active_form = 'form_3'

                return render(request, 'projects/commitment.html', {
                    'active_form': active_form,
                    'form1': CommitmentForm1(instance=proj),
                    'form2': CommitmentForm2(instance=proj),
                    'form3': CommitmentForm3(instance=proj),
                    'project': proj
                })

            else:
                active_form = 'form_2'
                return render(request, 'projects/commitment.html', {
                    'active_form': active_form,
                    'form1': CommitmentForm1(instance=proj),
                    'form2': form_2,
                    'form3': CommitmentForm3(instance=proj),
                    'project': proj
                })

        elif 'commitment_form_3' in request.POST:
            proj = Innovation.objects.get(lead__email=request.user.email)
            form_3 = CommitmentForm3(request.POST, request.FILES, instance=proj)

            if form_3.is_valid():
                proj_form = form_3.save(commit=False)
                proj_form.save()

                return HttpResponseRedirect(reverse('projects:view-startup'))

            else:
                active_form = 'form_3'
                return render(request, 'projects/commitment.html', {
                    'active_form': active_form,
                    'form1': CommitmentForm1(instance=proj),
                    'form2': CommitmentForm2(instance=proj),
                    'form3': form_3,
                    'project': proj
                })

    else:
        print "commitment get"
        return render(request, 'projects/commitment.html', {
            'active_form': active_form,
            'form1': CommitmentForm1(instance=proj),
            'form2': CommitmentForm2(instance=proj),
            'form3': CommitmentForm3(instance=proj),
            'project': proj
        })


def concepting_view(request):
    proj = Innovation.objects.get(lead__email=request.user.email)

    concepting_form_1 = ConceptingForm1(request.FILES, instance=proj)
    concepting_form_2 = ConceptingForm2(request.FILES, instance=proj)
    concepting_form_3 = ConceptingForm3(request.FILES, instance=proj)

    active_form = 'form_1'

    if request.method == 'POST':
        print request.POST
        proj = Innovation.objects.get(lead__email=request.user.email)
        concepting_form_1 = ConceptingForm1(request.POST, request.FILES, instance=proj)

        if 'concepting_form_1' in request.POST:
            concepting_form_1 = ConceptingForm1(request.POST, request.FILES)
            if concepting_form_1.is_valid():
                proj = Innovation.objects.get(lead__email=request.user.email)
                cleaned_data = concepting_form_1.cleaned_data
                proj.name = cleaned_data.get('name')
                proj.description = cleaned_data.get('description')
                proj.sectors = cleaned_data.get('sectors')
                proj.other_sectors = cleaned_data.get('other_sectors')
                proj.logo = cleaned_data.get('logo')
                proj.challenge_faced = cleaned_data.get("challenge_faced")
                proj.challenge_to_solve = cleaned_data.get("challenge_to_solve")
                proj.url = cleaned_data.get('url')

                proj.stage = 3
                proj.save()

                active_form = 'form_2'

                return render(request, 'projects/concepting.html', {
                    'active_form': active_form,
                    'form1': ConceptingForm1(instance=proj),
                    'form2': ConceptingForm2(instance=proj),
                    'form3': ConceptingForm3(instance=proj),
                    'project': proj
                })

            else:
                active_form = 'form_1'
                return render(request, 'projects/concepting.html', {
                    'active_form': active_form,
                    'form1': concepting_form_1,
                    'form2': ConceptingForm2(instance=proj),
                    'form3': ConceptingForm3(instance=proj),
                    'project': proj
                })

        elif 'concepting_form_2' in request.POST:
            proj = Innovation.objects.get(lead__email=request.user.email)
            form_2 = ConceptingForm2(request.POST, request.FILES, instance=proj)
            if form_2.is_valid():
                proj_form = form_2.save(commit=False)
                proj_form.save()

                active_form = 'form_3'

                return render(request, 'projects/concepting.html', {
                    'active_form': active_form,
                    'form1': ConceptingForm1(instance=proj),
                    'form2': ConceptingForm2(instance=proj),
                    'form3': ConceptingForm3(instance=proj),
                    'project': proj
                })

            else:
                active_form = 'form_2'
                return render(request, 'projects/concepting.html', {
                    'active_form': active_form,
                    'form1': ConceptingForm1(instance=proj),
                    'form2': form_2,
                    'form3': ConceptingForm3(instance=proj),
                    'project': proj
                })

        elif 'concepting_form_3' in request.POST:
            proj = Innovation.objects.get(lead__email=request.user.email)
            form_3 = ConceptingForm3(request.POST, request.FILES, instance=proj)

            if form_3.is_valid():
                proj_form = form_3.save(commit=False)
                proj_form.save()

                return HttpResponseRedirect(reverse('projects:view-startup'))

            else:
                active_form = 'form_3'
                return render(request, 'projects/concepting.html', {
                    'active_form': active_form,
                    'form1': ConceptingForm1(instance=proj),
                    'form2': ConceptingForm2(instance=proj),
                    'form3': form_3,
                    'project': proj
                })

    else:
        print "concepting get"
        return render(request, 'projects/concepting.html', {
            'active_form': active_form,
            'form1': ConceptingForm1(instance=proj),
            'form2': ConceptingForm2(instance=proj),
            'form3': ConceptingForm3(instance=proj),
            'project': proj
        })


def validation_view(request):
    proj = Innovation.objects.get(lead__email=request.user.email)

    validation_form_1 = ValidationForm1(request.FILES, instance=proj)
    validation_form_2 = ValidationForm2(request.FILES, instance=proj)
    validation_form_3 = ValidationForm3(request.FILES, instance=proj)

    active_form = 'form_1'

    if request.method == 'POST':
        print request.POST
        proj = Innovation.objects.get(lead__email=request.user.email)
        validation_form_1 = ValidationForm1(request.POST, request.FILES, instance=proj)

        if 'validation_form_1' in request.POST:
            validation_form_1 = ValidationForm1(request.POST, request.FILES)
            if validation_form_1.is_valid():
                proj = Innovation.objects.get(lead__email=request.user.email)
                cleaned_data = validation_form_1.cleaned_data
                proj.name = cleaned_data.get('name')
                proj.description = cleaned_data.get('description')
                proj.sectors = cleaned_data.get('sectors')
                proj.other_sectors = cleaned_data.get('other_sectors')
                proj.logo = cleaned_data.get('logo')
                proj.service_pic = cleaned_data.get('service_pic')
                proj.service_videos = cleaned_data.get('service_videos')
                proj.challenge_faced = cleaned_data.get("challenge_faced")
                proj.challenge_to_solve = cleaned_data.get("challenge_to_solve")
                proj.url = cleaned_data.get('url')

                proj.stage = 4
                proj.save()

                active_form = 'form_2'

                return render(request, 'projects/validation.html', {
                    'active_form': active_form,
                    'form1': ValidationForm1(instance=proj),
                    'form2': ValidationForm2(instance=proj),
                    'form3': ValidationForm3(instance=proj),
                    'project': proj
                })

            else:
                active_form = 'form_1'
                return render(request, 'projects/validation.html', {
                    'active_form': active_form,
                    'form1': validation_form_1,
                    'form2': ValidationForm2(instance=proj),
                    'form3': ValidationForm3(instance=proj),
                    'project': proj
                })

        elif 'validation_form_2' in request.POST:
            proj = Innovation.objects.get(lead__email=request.user.email)
            form_2 = ValidationForm2(request.POST, request.FILES, instance=proj)
            if form_2.is_valid():
                proj_form = form_2.save(commit=False)
                proj_form.save()

                active_form = 'form_3'

                return render(request, 'projects/validation.html', {
                    'active_form': active_form,
                    'form1': ValidationForm1(instance=proj),
                    'form2': ValidationForm2(instance=proj),
                    'form3': ValidationForm3(instance=proj),
                    'project': proj
                })

            else:
                active_form = 'form_2'
                return render(request, 'projects/validation.html', {
                    'active_form': active_form,
                    'form1': ValidationForm1(instance=proj),
                    'form2': form_2,
                    'form3': ValidationForm3(),
                    'project': proj
                })

        elif 'validation_form_3' in request.POST:
            proj = Innovation.objects.get(lead__email=request.user.email)
            form_3 = ValidationForm3(request.POST, request.FILES, instance=proj)

            if form_3.is_valid():
                proj_form = form_3.save(commit=False)
                proj_form.save()

                return HttpResponseRedirect(reverse('projects:view-startup'))

            else:
                active_form = 'form_3'
                return render(request, 'projects/validation.html', {
                    'active_form': active_form,
                    'form1': ValidationForm1(instance=proj),
                    'form2': ValidationForm2(instance=proj),
                    'form3': form_3,
                    'project': proj
                })

    else:
        print "validation get"
        return render(request, 'projects/validation.html', {
            'active_form': active_form,
            'form1': ValidationForm1(instance=proj),
            'form2': ValidationForm2(instance=proj),
            'form3': ValidationForm3(instance=proj),
            'project': proj
        })


def scaling_view(request):
    proj = Innovation.objects.get(lead__email=request.user.email)

    scaling_form_1 = ScalingForm1(request.FILES, instance=proj)
    scaling_form_2 = ScalingForm2(request.FILES, instance=proj)
    scaling_form_3 = ScalingForm3(request.FILES, instance=proj)

    active_form = 'form_1'

    if request.method == 'POST':
        # print request.POST
        proj = Innovation.objects.get(lead__email=request.user.email)
        scaling_form_1 = ScalingForm1(request.POST, request.FILES, instance=proj)

        if 'scaling_form_1' in request.POST:
            scaling_form_1 = ScalingForm1(request.POST, request.FILES)
            print scaling_form_1.data
            if scaling_form_1.is_valid():
                proj = Innovation.objects.get(lead__email=request.user.email)
                cleaned_data = scaling_form_1.cleaned_data
                proj.name = cleaned_data.get('name')
                proj.description = cleaned_data.get('description')
                proj.sectors = cleaned_data.get('sectors')
                proj.other_sectors = cleaned_data.get('other_sectors')
                proj.logo = cleaned_data.get('logo')
                proj.service_pic = cleaned_data.get('service_pic')
                proj.service_videos = cleaned_data.get('service_videos')
                proj.challenge_faced = cleaned_data.get("challenge_faced")
                proj.challenge_to_solve = cleaned_data.get("challenge_to_solve")
                proj.url = cleaned_data.get('url')

                proj.stage = 5
                proj.save()

                active_form = 'form_2'

                return render(request, 'projects/scaling.html', {
                    'active_form': active_form,
                    'form1': ScalingForm1(instance=proj),
                    'form2': ScalingForm2(instance=proj),
                    'form3': ScalingForm3(instance=proj),
                    'project': proj
                })

            else:
                active_form = 'form_1'
                return render(request, 'projects/scaling.html', {
                    'active_form': active_form,
                    'form1': scaling_form_1,
                    'form2': ScalingForm2(instance=proj),
                    'form3': ScalingForm3(instance=proj),
                    'project': proj
                })

        elif 'scaling_form_2' in request.POST:
            proj = Innovation.objects.get(lead__email=request.user.email)
            form_2 = ScalingForm2(request.POST, request.FILES, instance=proj)
            if form_2.is_valid():
                proj_form = form_2.save(commit=False)
                proj_form.save()

                active_form = 'form_3'

                return render(request, 'projects/scaling.html', {
                    'active_form': active_form,
                    'form1': ScalingForm1(instance=proj),
                    'form2': ScalingForm2(instance=proj),
                    'form3': ScalingForm3(instance=proj),
                    'project': proj
                })

            else:
                active_form = 'form_2'
                return render(request, 'projects/scaling.html', {
                    'active_form': active_form,
                    'form1': ScalingForm1(instance=proj),
                    'form2': form_2,
                    'form3': ScalingForm3(instance=proj),
                    'project': proj
                })

        elif 'scaling_form_3' in request.POST:
            proj = Innovation.objects.get(lead__email=request.user.email)
            form_3 = ScalingForm3(data=request.POST, files=request.FILES, instance=proj)
            cleaned_data = form_3.data
            print form_3.data

            if form_3.is_valid():
                proj_form = form_3.save(commit=False)
                if request.FILES:
                    if request.FILES['monthly_costs']:
                        proj_form.monthly = request.FILES['monthly_costs']
                    elif request.FILES['annual_costs']:
                        proj_form.annual = request.FILES['annual_costs']

                proj_form.save()

                proj.save()

                return HttpResponseRedirect(reverse('projects:view-startup'))

            else:
                active_form = 'form_3'
                return render(request, 'projects/scaling.html', {
                    'active_form': active_form,
                    'form1': ScalingForm1(instance=proj),
                    'form2': ScalingForm2(instance=proj),
                    'form3': form_3,
                    'project': proj
                })

    else:
        print "scaling get"
        return render(request, 'projects/scaling.html', {
            'active_form': active_form,
            'form1': ScalingForm1(instance=proj),
            'form2': ScalingForm2(instance=proj),
            'form3': ScalingForm3(instance=proj),
            'project': proj
        })


def establishing_view(request):
    proj = Innovation.objects.get(lead__email=request.user.email)

    establishing_form_1 = EstablishingForm1(request.FILES, instance=proj)
    establishing_form_2 = EstablishingForm2(request.FILES, instance=proj)
    establishing_form_3 = EstablishingForm3(request.FILES, instance=proj)

    active_form = 'form_1'

    if request.method == 'POST':
        print request.POST
        proj = Innovation.objects.get(lead__email=request.user.email)
        establishing_form_1 = EstablishingForm1(request.POST, request.FILES, instance=proj)

        if 'establishing_form_1' in request.POST:
            establishing_form_1 = EstablishingForm1(request.POST, request.FILES)
            if establishing_form_1.is_valid():
                print "establishing form is valid"
                proj = Innovation.objects.get(lead__email=request.user.email)
                cleaned_data = establishing_form_1.cleaned_data
                proj.name = cleaned_data.get('name')
                proj.description = cleaned_data.get('description')
                proj.sectors = cleaned_data.get('sectors')
                proj.other_sectors = cleaned_data.get('other_sectors')
                proj.logo = cleaned_data.get('logo')
                proj.service_pic = cleaned_data.get('service_pic')
                proj.service_videos = cleaned_data.get('service_videos')
                proj.challenge_faced = cleaned_data.get("challenge_faced")
                proj.challenge_to_solve = cleaned_data.get("challenge_to_solve")
                proj.url = cleaned_data.get('url')

                proj.stage = 6
                proj.save()

                active_form = 'form_2'

                return render(request, 'projects/establishing.html', {
                    'active_form': active_form,
                    'form1': EstablishingForm1(instance=proj),
                    'form2': EstablishingForm2(instance=proj),
                    'form3': EstablishingForm3(instance=proj),
                    'project': proj
                })

            else:
                print "establishing form is valid"
                active_form = 'form_1'
                return render(request, 'projects/establishing.html', {
                    'active_form': active_form,
                    'form1': establishing_form_1,
                    'form2': EstablishingForm2(instance=proj),
                    'form3': EstablishingForm3(instance=proj),
                    'project': proj
                })

        elif 'establishing_form_2' in request.POST:
            proj = Innovation.objects.get(lead__email=request.user.email)
            form_2 = EstablishingForm2(request.POST, request.FILES, instance=proj)
            if form_2.is_valid():
                proj_form = form_2.save(commit=False)
                proj_form.save()

                active_form = 'form_3'

                return render(request, 'projects/establishing.html', {
                    'active_form': active_form,
                    'form1': EstablishingForm1(instance=proj),
                    'form2': EstablishingForm2(instance=proj),
                    'form3': EstablishingForm3(instance=proj),
                    'project': proj
                })

            else:
                active_form = 'form_2'
                return render(request, 'projects/establishing.html', {
                    'active_form': active_form,
                    'form1': EstablishingForm1(instance=proj),
                    'form2': form_2,
                    'form3': EstablishingForm3(instance=proj),
                    'project': proj
                })

        elif 'establishing_form_3' in request.POST:
            proj = Innovation.objects.get(lead__email=request.user.email)
            form_3 = EstablishingForm3(request.POST, request.FILES, instance=proj)

            if form_3.is_valid():
                proj_form = form_3.save(commit=False)
                if request.FILES:
                    if request.FILES['monthly_costs']:
                        proj_form.monthly = request.FILES['monthly_costs']
                    elif request.FILES['annual_costs']:
                        proj_form.annual = request.FILES['annual_costs']
                proj_form.save()

                return HttpResponseRedirect(reverse('projects:view-startup'))

            else:
                active_form = 'form_3'
                return render(request, 'projects/establishing.html', {
                    'active_form': active_form,
                    'form1': EstablishingForm1(instance=proj),
                    'form2': EstablishingForm2(instance=proj),
                    'form3': form_3,
                    'project': proj
                })

    else:
        print "establishing get"
        return render(request, 'projects/establishing.html', {
            'active_form': active_form,
            'form1': EstablishingForm1(instance=proj),
            'form2': EstablishingForm2(instance=proj),
            'form3': EstablishingForm3(instance=proj),
            'project': proj
        })


def edit_startups_view(request):
    request.session['status'] = 'edit'
    proj = Innovation.objects.get(lead__email=request.user.email)
    print "proj stage: ", proj.stage
    if proj.stage == '1':
        return HttpResponseRedirect(reverse('projects:ideation'))
    elif proj.stage == '2':
        return HttpResponseRedirect(reverse('projects:commitment'))
    elif proj.stage == '3':
        return HttpResponseRedirect(reverse('projects:concepting'))
    elif proj.stage == '4':
        return HttpResponseRedirect(reverse('projects:validation'))
    elif proj.stage == '5':
        return HttpResponseRedirect(reverse('projects:scaling'))
    elif proj.stage == '6':
        return HttpResponseRedirect(reverse("projects:establishing"))
    else:
        return HttpResponseRedirect(reverse('index:home'))

