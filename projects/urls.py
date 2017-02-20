from django.conf.urls import url
from projects.views import EditInvestmentCompany

urlpatterns = [
    url(r'^investment_company', EditInvestmentCompany.as_view(), name='investment_company'),
]
