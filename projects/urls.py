from django.conf.urls import url
from projects.views import EditInvestmentCompany, select_startup_stage

urlpatterns = [
    url(r'^investment_company', EditInvestmentCompany.as_view(), name='investment_company'),
    url(r'startup-stage', select_startup_stage, name='select-startup-stage'),
]
