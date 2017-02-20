from django.shortcuts import render
from django.views.generic import FormView
from projects.investor_form import InvestorForm

# Create your views here.


class EditInvestmentCompany(FormView):
    form_class = InvestorForm
    template_name = 'projects/investor_profile_wizard.html'