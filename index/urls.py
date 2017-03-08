from django.conf.urls import url
from index.views import homepage, verify, verify_key, logout, ResetPasswordView, signin, register, confirm_password,\
    email_sent, signup_success, password_reset_expired, RecoverAccountView

urlpatterns = [
    url(r'^$', homepage, name='home'),
    url(r'^verify$', verify, name='verify'),
    url(r'^password/reset/expired$', password_reset_expired, name='password-reset-expired'),
    url(r'^signup-success$', signup_success, name='signup-success'),
    url(r'^email-sent$', email_sent, name='email-sent'),
    url(r'^signin$', signin, name='signin'),
    url(r'^register$', register, name='register'),
    url(r'^logout$', logout, name='logout'),
    url(r'^verify/(?P<key>\w+)/', verify_key, name='verify_key'),
    url(r'password$', ResetPasswordView.as_view(), name='password'),
    url(r'account/recover$', RecoverAccountView.as_view(), name='recover-account'),
    url(r'confirm_password/(?P<key>\w+)/', confirm_password, name='confirm_password'),
]
