from django.conf.urls import url
from users.views import ViewProfile, view_profile, EditInnovator, EditHubManager, EditInvestor, EditMentor

urlpatterns = [
    url(r'^view', view_profile, name='view_profile'),
    url(r'edit/(?P<pk>\d+)/mentor$', EditMentor.as_view(), name='edit-mentor'),
    url(r'edit/(?P<pk>\d+)/investor$', EditInvestor.as_view(), name='edit-investor'),
    url(r'edit/(?P<pk>\d+)/innovator$', EditInnovator.as_view(), name='edit-innovator'),
    url(r'edit/(?P<pk>\d+)/hub/manager$', EditHubManager.as_view(), name='edit-hub-manager'),
]