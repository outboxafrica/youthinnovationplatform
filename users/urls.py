from django.conf.urls import url
from users.views import EditUser, ViewProfile

urlpatterns = [
    url(r'^edit$', EditUser.as_view(), name='edit_user'),
    url(r'^view', ViewProfile.as_view(), name='view_profile'),
]