from django.conf.urls import url
from events.views import EventsIndex, EventsDetail

app_name = "pm"

# Project Create
urlpatterns = [
    url(r'^current', EventsIndex.as_view(), name='events_index'),
    url(r'^view/(?P<pk>\d+)/detail', EventsDetail.as_view(), name='detail'),
]
