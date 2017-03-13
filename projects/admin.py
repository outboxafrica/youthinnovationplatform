from django.contrib import admin
from projects.models import Innovation, InvestmentCompany, CommunityHub

# Register your models here.
admin.site.register(Innovation)
admin.site.register(InvestmentCompany)
admin.site.register(CommunityHub)
