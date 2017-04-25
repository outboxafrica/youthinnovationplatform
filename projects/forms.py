from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineCheckboxes
from projects.models import Innovation, InvestmentCompany
from projects.validators import validate_img
from YouthInnovPltfrm.forms import BaseForm, BaseModelForm


class StartupStageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StartupStageForm, self).__init__(*args, **kwargs)
        self.fields['idea_stage'].label = "Please select the stage of your startup"
    idea_stage = forms.ChoiceField(
        choices=(('1', "I have an idea"),
                 ('2', "I have an idea and have something to show"),
                 ('3', "I'm thinking about target and direction for my idea"),
                 ('4', "I'm testing my business with actual users"),
                 ('5', "I'm looking to grow my business"),
                 ('6', "I'm looking to maintain growth"), ),
        widget=forms.RadioSelect, required=True)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('idea_stage'),
        FormActions(
            HTML('<a class="cancelBtn btn btn-primary" href={% url "index:home" %}>Cancel</a>'),
            Submit(
                'next',
                'Save and Next',
                css_class="cancelBtn"
            ),
        ),
    )

    class Meta:
        model = Innovation
        fields = ('idea_stage', )


class IdeationStage(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super(IdeationStage, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Idea name"
        self.fields['description'].label = "Please describe your idea"
        self.fields['sectors'].label = "What sectors do you operate in?"
        self.fields['challenge_to_solve'].label = "What problems/Challenges or needs is your idea trying to solve?"
        self.fields['challenge_faced'].label = "What challenges are you facing?"
        self.fields['other_challenges'].label = ""

    name = forms.CharField(widget=forms.TextInput(attrs={'class': "", 'placeholder': 'name of idea'}))
    description = forms.CharField(widget=forms.Textarea())
    idea_stage = forms.CharField(required=False)
    sectors = forms.MultipleChoiceField(
        choices=(
            ('agriculture', "Agriculture"),
            ('manufacturing', "Manufacturing and Assembly"),
            ('financial', "Financial Services"),
            ('renewable', "Renewable Energy"),
            ('information security', "Information Security"),
            ('education', "Education"),
            ('health', "Healthcare & Services"),
            ('infrastructure', "Infrastructure"),
            ('transport', "Transport"),
        ),
        widget=forms.CheckboxSelectMultiple,
    )
    other_sectors = forms.CharField(required=False, max_length=2000)
    challenge_to_solve = forms.CharField(widget=forms.Textarea())
    other_challenges = forms.CharField(widget=forms.Textarea(), required=False)
    challenge_faced = forms.MultipleChoiceField(
        choices=(
            ('mentorship', "Mentorship"),
            ('office space', "Office Space"),
            ('networking', "To network"),
            ('training', "Training on how to run a business"),
            ('technical', "Technical Training"),
            ('team', "To build a team"),
            ('funding', "Funding"),
            ('others', "Others"),
        ),
        widget=forms.CheckboxSelectMultiple,
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('name', css_class='text-small'),
        Field('description', rows="4", css_class='text-large'),
        Field('sectors', ),
        Field('other_sectors',
              css_class='text-small'),
        Field('challenge_to_solve', rows="4", css_class='text-large'),
        Field('challenge_faced', css_class=''),
        Field('other_challenges', css_class='text-small', placeholder="Other Challenges"),
        FormActions(
            Button('cancel', 'Cancel', css_class='cancelBtn'),
            Submit(
                'next',
                'Finish',
                css_class="cancelBtn"
            ),
        ),
    )

    class Meta:
        model = Innovation
        fields = ('name', 'description', 'sectors', 'other_sectors', 'challenge_faced', 'challenge_to_solve',
                  'other_challenges')


class InvestmentCompanyForm(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super(InvestmentCompanyForm, self).__init__(*args, **kwargs)
        self.fields['preferred_industries'].label = 'Please select your prefered industries'
        self.fields['investment_stage'].label = 'At what stage do you support investments?'
        self.fields['ticket_size'].label = 'Please tell us your ticket size for investments?'
        self.fields['url'].label = 'What is your organisation URL?'
        self.fields['logo'].label = "Organisation logo (jpeg, png, gif)"

    investor_focus = forms.CharField(widget=forms.Textarea(), label="Please describe the investor focus of your organisation")
    preferred_industries = forms.MultipleChoiceField(
        choices=(
            ('agriculture', "Agriculture"),
            ('manufacturing', "Manufacturing and Assembly"),
            ('financial', "Financial Services"),
            ('renewable', "Renewable Energy"),
            ('information security', "Information Security"),
            ('education', "Education"),
            ('health', "Healthcare & Services"),
            ('infrastructure', "Infrastructure"),
            ('transport', "Transport"),
        ), required=True)
    other_industries = forms.CharField()
    investment_stage = forms.MultipleChoiceField(
        choices=(
            ("Concept Stage", "Concept stage"),
            ("Seed stage (finding product market fit)", "Seed stage (finding product market fit)"),
            ("Venture captial (growth)", "Venture captial (growth)"),
            ("Private Equity (scaling and expansion)", "Private Equity (scaling and expansion)")
        ), required=True)
    ticket_size = forms.CharField(required=True)
    url = forms.CharField()
    logo = forms.ImageField(validators=[validate_img], required=False)
    organisation_name = forms.CharField()

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('organisation_name', css_class='text-small form-control'),
        Field('logo'),
        Field('url', css_class='text-small form-control'),
        Field('ticket_size', css_class='text-small form-control'),
        InlineCheckboxes('preferred_industries'),
        Field('other_industries', css_class='text-small form-control'),
        Field('investor_focus', css_class='text-large form-control'),
        InlineCheckboxes('investment_stage'),
        FormActions(
            Button('cancel', 'Cancel', css_class='cancelBtn'),
            Submit(
                'next',
                'Finish',
                css_class="cancelBtn"
            ),
        ),
    )

    class Meta:
        model = InvestmentCompany
        fields = [
            'investor_focus', 'preferred_industries', 'other_industries', 'investment_stage', 'ticket_size', 'logo',
            'url', 'organisation_name'
        ]


