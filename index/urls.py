from django.conf.urls import url
from index.views import HomePageView, verify, verify_key, logout, ResetPasswordView, signin, register, confirm_password

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^verify$', verify, name='verify'),
    url(r'^signin$', signin, name='signin'),
    url(r'^register$', register, name='register'),
    url(r'^logout$', logout, name='logout'),
    url(r'^verify/(?P<key>\w+)/', verify_key, name='verify_key'),
    url(r'password$', ResetPasswordView.as_view(), name='password'),
    url(r'confirm_password/(?P<key>\w+)/', confirm_password, name='confirm_password'),
]
