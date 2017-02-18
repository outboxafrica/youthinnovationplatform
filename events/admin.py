from django.contrib import admin
from events.models import Event, Occurrence

# Register your models here.


class Occurrenceline(admin.StackedInline):
    model = Occurrence
    extra = 1
    max_num = 1
    verbose_name = "Event time"
    verbose_name_plural = "Event time"


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "venue", "price")
    inlines = (Occurrenceline,)

admin.site.register(Event, EventAdmin)
admin.site.register(Occurrence)