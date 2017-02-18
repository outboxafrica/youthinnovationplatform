from django.conf.urls import url
from index.views import HomePageView, accounts

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'accounts', accounts, name='accounts'),
url(r'^verify$', verify, name='verify'),
    url(r'^verify/(?P<key>\w+)/', verify_key, name='verify_key'),
]