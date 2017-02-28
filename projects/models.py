from __future__ import unicode_literals

from django.db import models
from users.models import Innovator
# Create your models here.


class InvestmentCompany(models.Model):
    investor_focus = models.TextField(blank=True)
    preferred_industries = models.CharField(max_length=200, blank=True)
    other_industries = models.CharField(max_length=100, blank=True)
    investment_stage = models.CharField(max_length=200, blank=True)
    ticket_size = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)
    logo = models.FileField(upload_to='static/logos/%Y/%m/%d/', blank=True)
    organisation_name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    support_type = models.CharField(max_length=255, blank=True)
    competencies = models.TextField(blank=True)
    specialties = models.TextField(blank=True)
    published = models.BooleanField(default=False)

    def get_logo(self):
        if self.logo:
            return self.logo.url
        elif self.picture:
            return self.picture.url
        else:
            return "/"

    def __unicode__(self):
        return self.organisation_name


class CommunityHub(models.Model):
    organisation_name = models.CharField(max_length=200, blank=True)
    hub_focus = models.TextField(blank=True)
    preferred_industries = models.CharField(max_length=200, blank=True)
    investment_stage = models.CharField(max_length=200, blank=True)
    support_type = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=200, blank=True)
    logo = models.FileField(upload_to='static/logos/%Y/%m/%d/', blank=True)

    def __unicode__(self):
        return self.organisation_name


class Innovation(models.Model):
    lead = models.ForeignKey(Innovator, null=True)
    stage = models.CharField(max_length=1, blank=True)
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=200, blank=True)
    service_pic = models.ImageField(upload_to='static/service_pics/%Y/%m/%d/',
                                    blank=True)
    service_videos = models.TextField(blank=True)
    sectors = models.TextField(blank=True)
    other_sectors = models.CharField(max_length=30, blank=True)
    challenge_to_solve = models.TextField(blank=True)
    challenge_faced = models.TextField(blank=True)
    logo = models.ImageField(upload_to='static/logos/%Y/%m/%d', blank=True)

    target_customers = models.TextField(blank=True)
    market_size = models.TextField(blank=True)
    customer_lessons = models.TextField(blank=True)
    acquisition_plan = models.TextField(blank=True)
    potential_competitors = models.TextField(blank=True)
    competitive_advantage = models.TextField(blank=True)
    business_differentiator = models.TextField(blank=True)
    major_wrongs = models.TextField(blank=True)

    revenue = models.TextField(blank=True)
    monthly_costs = models.FileField(upload_to='static/uploads/%Y/%m/%d/', blank=True)
    annual_costs = models.FileField(upload_to='static/uploads/%Y/%m/%d/', blank=True)

    growth_ambitions = models.TextField(blank=True)
    milestones = models.TextField(blank=True)

    do_you_have_audited_books = models.CharField(max_length=50, blank=True)
    total_sales = models.CharField(max_length=50, blank=True)
    total_capital = models.CharField(max_length=50, blank=True)
    expected_capital = models.CharField(max_length=50, blank=True)
    capital_type = models.CharField(max_length=50, blank=True)
    capital_use = models.CharField(max_length=50, blank=True)

    test_plan = models.TextField(blank=True)
    impact_measure_plan = models.TextField(blank=True)
    show_success_plan = models.TextField(blank=True)

    costs = models.TextField(max_length=50, blank=True)

    do_really_well = models.TextField(blank=True)
    key_resources = models.TextField(blank=True)
    key_partners = models.TextField(blank=True)

    problem_change = models.TextField(blank=True)
    customer_change = models.TextField(blank=True)
    planned_acquisition_plan = models.TextField(blank=True)
    performance = models.TextField(blank=True)
    test_learnings = models.TextField(blank=True)

    monthly_cashflow = models.FileField(
        upload_to='static/cashflows/%Y/%m/%d/',
        blank=True)
    income_statement = models.FileField(
        upload_to='static/income_statements/%Y/%m/%d/',
        blank=True)
    published = models.BooleanField(default=False)

    def get_logo(self):
        try:
            return self.logo.url
        except:
            return "/"

    def audited_books(self):
        try:
            vals = ["No", "Yes"]
            return vals[int(self.do_you_have_auditedbooks)]
        except:
            return "No"

    def type_of_capital_sought(self):
        try:
            vals = ["", "Equity", "Grants", "Convertible Debt",
                    "Commercial Debt (Banks)", "Soft Debt (Friends)"]
            return vals[int(self.capital_type)]
        except:
            return ""

        # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.name

    @property
    def __str__(self):
        return self.name
