from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from projects.models import InvestmentCompany
from users.models import User, Innovator
from projects.investor_form import InvestorForm
from projects.forms import StartupStageForm

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

            innov.has_startup = True
            innov.save()

            if stage == 1:
                # idea
                return HttpResponseRedirect('/projects/idea_wizard/')
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
            return render(request, 'users/startup_stage.html', {'form': form})

    else:
        return render(request, 'users/startup_stage.html', {'form': form})