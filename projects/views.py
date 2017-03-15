from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView, UpdateView
from projects.models import InvestmentCompany, Innovation
from users.models import User, Innovator
from projects.investor_form import InvestorForm
from projects.forms import StartupStageForm, IdeationStage

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
                return HttpResponseRedirect('/projects/idea_show/')
            elif stage == 3:
                # target and direction
                return HttpResponseRedirect('/projects/target_direction/')
            elif stage == 4:
                # testing with actual users
                return HttpResponseRedirect('/projects/testing_users/')
            elif stage == 5:
                # grow business
                return HttpResponseRedirect('/projects/grow_business/')
            elif stage == 6:
                # maintain growth
                return HttpResponseRedirect('/projects/maintain_growth/')

        else:
            form = StartupStageForm(request.POST)
            return render(request, 'projects/startup_stage.html', {'form': form})

    else:
        return render(request, 'projects/startup_stage.html', {'form': form})


def ideation(request):
    form = IdeationStage()
    if request.method == "POST":
        form = IdeationStage(request.POST)
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

            proj.stage = 0
            proj.save()
            return HttpResponseRedirect(reverse("index:home"))
        else:
            return render(request, "projects/idea_wizard.html", {'form': form})
    else:
        return render(request, "projects/idea_wizard.html", {'form': form})


def view_startup(request):
    innovation_profile = get_object_or_404(Innovation, lead=request.user.id)
    return render(request, 'projects/view_startup.html', {'project': innovation_profile})


def edit_startup_profile(request):
    innovation_profile = get_object_or_404(Innovation, lead=request.user.id)
    if request.method == 'POST':
        form = IdeationStage(request.POST, instance=innovation_profile)
        if form.is_valid():
            idea_form = form.save(commit=False)
            idea_form.idea_stage = 1
            try:
                idea_form.save()
            except:
                print 'errors'
            # print idea_form
            return HttpResponseRedirect(reverse('projects:view-startup'))

        else:
            print 'errors'
            print form.errors
    else:
        form = IdeationStage(instance=innovation_profile)
    form = IdeationStage(instance=innovation_profile)
    return render(request, 'projects/idea_wizard.html', {'form': form})


class EditIdeationProfile(UpdateView):
    form_class = IdeationStage
