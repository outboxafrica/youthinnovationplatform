from django.conf.urls import url
from projects.views import EditInvestmentCompany, select_startup_stage, ideation, view_startup, edit_startup_profile, \
    commitment_view, concepting_view, validation_view, scaling_view, establishing_view

urlpatterns = [
    url(r'^investment_company', EditInvestmentCompany.as_view(), name='investment_company'),
    url(r'startup-stage', select_startup_stage, name='select-startup-stage'),
    url(r'ideation', ideation, name="ideation"),
    url(r'view-startup', view_startup, name="view-startup"),
    url(r'edit-startup', edit_startup_profile, name="edit-startup"),
    url(r'commitment-stage', commitment_view, name="commitment"),
    url(r'concepting-stage', concepting_view, name="concepting"),
    url(r'validation-stage', validation_view, name="validation"),
    url(r'scaling-stage', scaling_view, name="scaling"),
    url(r'establishing-stage', establishing_view, name="establishing"),
]
