from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from users.models import InvestmentCompany, User
from projects.investor_form import InvestorForm

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
