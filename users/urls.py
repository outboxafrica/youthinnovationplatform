from django.conf.urls import url
from users.views import EditUser, ViewProfile, view_profile

urlpatterns = [
    url(r'^edit$', EditUser.as_view(), name='edit_user'),
    url(r'^view', view_profile, name='view_profile'),

]