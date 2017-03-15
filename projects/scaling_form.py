from django.contrib.auth.models import User
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineCheckboxes
from projects.models import Innovation
from projects.validators import validate_img, validate_xls
from YouthInnovPltfrm.forms import BaseModelForm


class ScalingForm1(BaseModelForm):

    def __init__(self, *args, **kwargs):
        super(ScalingForm1, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Company name"
        self.fields['description'].label = "Please describe your business"
        self.fields[
            'url'].label = "Please share a url to the website with your product"
        self.fields['sectors'].label = "What sectors do you operate in?"
        self.fields[
            'service_pic'].label = "Please provide a picture that shows your product/service (jpeg, png, gif)"
        self.fields[
            'service_videos'].label = "Please provide a link to the video that shows your product/service. [This can be a link to youtube or vimeo]"
        self.fields[
            'challenge_to_solve'].label = "What problems/Challenges or needs is your idea trying to solve?"
        self.fields[
            'challenge_faced'].label = "What challenges are you facing?"

    name = forms.CharField()
    logo = forms.ImageField(validators=[validate_img])
    service_pic = forms.ImageField(required=False)
    service_videos = forms.URLField(required=False)
    url = forms.URLField(required=False)
    description = forms.CharField(widget=forms.Textarea(), )
    sectors = forms.MultipleChoiceField(
        required=False,
        choices=(('agriculture', "Agriculture"),
                 ('manufacturing', "Manufacturing and Assembly"),
                 ('financial', "Financial Services"),
                 ('renewable', "Renewable Energy"),
                 ('infosec', "Information Security"),
                 ('education', "Education"),
                 ('health', "Healthcare & Services"),
                 ('infrastructure', "Infrastructure"),
                 ('transport', "Transport"), ),
        widget=forms.CheckboxSelectMultiple,
    )

    challenge_to_solve = forms.CharField(widget=forms.Textarea(), )

    challenge_faced = forms.MultipleChoiceField(
        choices=(('financial_articulation', "I can't articulate my financials"),
                 ('risk_management', "I do not know how to manage risk"),
                 ('runway_ending', "Running out of start up capital"),
                 ('business_differentiator', "Figuring out why my business is different"),
                 ('team_members', "Getting qualified team members"), ),
        widget=forms.CheckboxSelectMultiple, )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('name',
              css_class='input-length form-control'),
        Field('description',
              rows="3",
              css_class='input-length form-control'),
        Field('url',
              css_class='input-length form-control'),
        Field('service_pic',
              css_class='input-length file-ubload'),
        Field('service_videos',
              css_class='input-length form-control'),
        InlineCheckboxes('sectors'),
        Field('other_sectors',
              css_class='input-length3 form-control'),
        Field('challenge_to_solve',
              rows="3",
              css_class='input-length form-control'),
        InlineCheckboxes('challenge_faced'),
        Field('logo',
              css_class='file-upload'),
        Div(
            Div(css_class="col-md-3 as-formactions-wrap as-top-20"), Div(css_class="col-md-6 as-form-progress as-top-20"),
            Div(
                FormActions(
                    Submit(
                        'next',
                        'Next',
                        css_class="btn-primary btn btn-block"
                    )
                ),
                css_class="col-md-3 as-top-20"
            ),
            css_class="row",
        ),
    )

    class Meta:
        model = Innovation
        fields = ('name', 'description', 'url', 'sectors', 'other_sectors', 'challenge_faced',
                  'challenge_to_solve', 'logo', 'service_pic',
                  'service_videos')


class ScalingForm2(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super(ScalingForm2, self).__init__(*args, **kwargs)
        self.fields[
            'target_customers'].label = "Who are your Target customers?"
        self.fields[
            'market_size'].label = "How big is the market facing this particular problem?"
        self.fields[
            'customer_lessons'].label = "The first time you tested your idea with customers, what are the three most important things you learned?"
        self.fields[
            'acquisition_plan'].label = "How do you currently reach your customers?"
        self.fields[
            'potential_competitors'].label = "Who are your potential competitors (or what other products/services address the same issue as yourself)?"
        self.fields[
            'competitive_advantage'].label = "Why can't a competitor replicate your plan tomorrow?"
        self.fields[
            'major_wrongs'].label = "What are the three major things that can go wrong during implementation?"
        self.fields[
            'business_differentiator'].label = "What differentiates your idea/business from alternative products/services?"

    target_customers = forms.CharField(widget=forms.Textarea())
    market_size = forms.CharField(widget=forms.Textarea())
    customer_lessons = forms.CharField(widget=forms.Textarea())
    acquisition_plan = forms.CharField(widget=forms.Textarea())
    potential_competitors = forms.CharField(widget=forms.Textarea())
    competitive_advantage = forms.CharField(widget=forms.Textarea())
    business_differentiator = forms.CharField(widget=forms.Textarea())
    major_wrongs = forms.CharField(widget=forms.Textarea())

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('target_customers',
              rows="3",
              css_class='form-control'),
        Field('market_size',
              rows="3",
              css_class='form-control'),
        Field('customer_lessons',
              rows="3",
              css_class='form-control'),
        Field('acquisition_plan',
              rows="3",
              css_class='form-control'),
        Field('potential_competitors',
              rows="3",
              css_class='form-control'),
        Field('competitive_advantage',
              rows="3",
              css_class='form-control'),
        Field('business_differentiator',
              rows="3",
              css_class='form-control'),
        Field('major_wrongs',
              rows="3",
              css_class='form-control'),
        Div(
            Div(css_class="col-md-3 as-formactions-wrap as-top-20"), Div(css_class="col-md-6 as-form-progress as-top-20"),
            Div(
                FormActions(
                    Submit(
                        'next',
                        'Next',
                        css_class="btn-primary btn btn-block"
                    )
                ),
                css_class="col-md-3 as-top-20"
            ),
            css_class="row",
        ),
    )

    class Meta:
        model = Innovation
        fields = ('target_customers', 'market_size', 'customer_lessons',
                  'acquisition_plan', 'potential_competitors',
                  'competitive_advantage', 'business_differentiator',
                  'major_wrongs')


class ScalingForm3(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super(ScalingForm3, self).__init__(*args, **kwargs)
        self.fields['revenue'].label = "What are your revenue sources?"
        self.fields['mcosts'].label = "What are your monthly operating costs?"
        self.fields['ycosts'].label = "What are your yearly operating costs?"
        self.fields[
            'growth_ambitions'].label = "What are your growth ambitions for the next 24 months?"
        self.fields[
            'milestones'].label = "What are the main milestones you've achieved in the last 6 months?"
        self.fields[
            'total_sales'].label = "What are your total sales in the last 12 months? (Optional)"
        self.fields[
            'do_you_have_auditedbooks'].label = "Do you have audited books for the last 3 years?"
        self.fields[
            'total_capital'].label = "How much capital have you raised since inception?"

        self.fields[
            'expected_capital'].label = "How much capital do you intend to raise?"
        self.fields['capital_type'].label = "What type of capital do you seek?"
        self.fields['capital_use'].label = "What's the capital intended for?"

    revenue = forms.CharField(widget=forms.Textarea())

    mcosts = forms.FileField(validators=[validate_xls])
    ycosts = forms.FileField(validators=[validate_xls])
    growth_ambitions = forms.CharField(widget=forms.Textarea())
    milestones = forms.CharField(widget=forms.Textarea())
    do_you_have_auditedbooks = forms.ChoiceField(
        choices=(('1', "Yes"), ('0', "No")),
        widget=forms.RadioSelect, )
    total_capital = forms.CharField()
    total_sales = forms.CharField(required=False)
    expected_capital = forms.CharField()
    capital_type = forms.ChoiceField(choices=(('1', "Equity"),
                                              ('2', "Grants"),
                                              ('3', "Convertible Debt"),
                                              ('4', "Commercial Debt (Banks)"),
                                              ('5', "Soft Debt (Friends)"), ),
                                     widget=forms.RadioSelect, )
    capital_use = forms.CharField()

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('revenue',
              rows="3",
              css_class='input-length1 form-control'),
        # Field('monthly_cashflow', css_class='file-upload'),
        # Field('income_statement', css_class='file-upload'),
        Field('mcosts'),
        Field('ycosts'),
        Field('growth_ambitions',
              rows="3",
              css_class='input-length1 form-control'),
        Field('milestones',
              rows="3",
              css_class='input-length1 form-control'),
        Field('total_sales',
              css_class='input-length1 form-control'),

        Field('do_you_have_auditedbooks'),
        Field('total_capital',
              css_class='input-length1 form-control'),
        Field('expected_capital',
              css_class='input-length1 form-control'),
        Field('capital_type'),
        Field('capital_use',
              css_class='input-length1 form-control'),
        Div(
            Div(css_class="col-md-3 as-formactions-wrap as-top-20"), Div(css_class="col-md-6 as-form-progress as-top-20"),
            Div(
                FormActions(
                    Submit(
                        'next',
                        'Submit',
                        css_class="btn-primary btn btn-block"
                    )
                ),
                css_class="col-md-3 as-top-20"
            ),
            css_class="row",
        ),
    )

    class Meta:
        model = Innovation
        fields = ('revenue', 'mcosts', 'ycosts', 'growth_ambitions',
                  'milestones', 'do_you_have_auditedbooks',
                  'total_capital', 'expected_capital', 'capital_type',
                  'capital_use', 'total_sales')
