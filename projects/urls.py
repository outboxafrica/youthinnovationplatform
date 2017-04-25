from django.conf.urls import url
from projects.views import select_startup_stage, ideation, view_startup, edit_startups_view, \
    commitment_view, concepting_view, validation_view, scaling_view, establishing_view, StartupDetailView, \
    CreateInvestmentCompany, UpdateInvestmentCompany

urlpatterns = [
    url(r'startup-stage', select_startup_stage, name='select-startup-stage'),
    url(r'ideation', ideation, name="ideation"),
    url(r'view-startup', view_startup, name="view-startup"),
    url(r'edit-startup', edit_startups_view, name="edit-startup"),
    url(r'commitment-stage', commitment_view, name="commitment"),
    url(r'concepting-stage', concepting_view, name="concepting"),
    url(r'validation-stage', validation_view, name="validation"),
    url(r'scaling-stage', scaling_view, name="scaling"),
    url(r'establishing-stage', establishing_view, name="establishing"),
    url(r'innovation/(?P<pk>\d+)/detail$', StartupDetailView.as_view(), name='startup-detail'),
    url(r'edit/(?P<pk>\d+)/investment/company$', UpdateInvestmentCompany.as_view(), name='update-investment-company'),
    url(r'create/investment/company', CreateInvestmentCompany.as_view(), name="create-investment-company"),

]
