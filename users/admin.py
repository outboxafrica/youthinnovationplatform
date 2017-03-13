from django.contrib import admin
from users.models import Innovator, Investor, HubManager, ProgramManager, Mentor

# Register your models here.

admin.site.register(Innovator)
admin.site.register(Investor)
admin.site.register(HubManager)
admin.site.register(ProgramManager)
admin.site.register(Mentor)
