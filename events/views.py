from django.shortcuts import render
from django.views.generic import ListView
from events.models import Event, Occurrence
from django.utils import timezone


def view(request, id):
    calendar_events = Event.objects.for_period(from_date=timezone.now())
    event = Event.objects.get(id=id)
    return render(request, 'events/view.html', {"event": event, "events": calendar_events, "now": timezone.now()})


class EventsIndex(ListView):
    model = Event
    template_name = "events/index.html"

    def get_context_data(self, **kwargs):
        context = super(EventsIndex, self).get_context_data(**kwargs)
        events = Event.objects.all().sort_by_next()
        if len(events) > 0:
            " if there are any upcoming events"
            upcoming_event = events[0]
            events = events[1:]
            context['upcoming_event'] = upcoming_event
            context['events'] = events
            return context
        else:
            context['no_event'] = True
            past_events = Event.objects.all()
            if len(past_events) < 8:
                " if the number of past events are less than 8, display all of them"
                context['past_events'] = past_events
                return context
            else:
                "if number of past events is more than 8, display the last 8 events"
                context['past_events'] = past_events[:8]
                return context
