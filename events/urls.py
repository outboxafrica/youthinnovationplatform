from django.conf.urls import url
from . import views
from events.views import EventsIndex

app_name = "pm"

# Project Create
urlpatterns = [
    url(r'^', EventsIndex.as_view(), name='events_index'),
    url(r'^view/(?P<id>[0-9]+)/', views.view, name='view'),
]
