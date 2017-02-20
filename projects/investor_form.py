from django.contrib.auth.models import User
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineCheckboxes
from users.models import InvestmentCompany

from projects.validators import validate_img


class InvestorBaseForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(InvestorBaseForm, self).clean()
        pref_industries = cleaned_data.get("preferred_industries")
        other_industries = cleaned_data.get("other_industries")
        if not pref_industries and not other_industries:
            msg = (
                "Please select one of the available industries or "
                "submit a new one."
            )
            self.add_error('preferred_industries', msg)
            self.add_error('other_industries', msg)
            raise forms.ValidationError(msg)
        return cleaned_data


class InvestorForm(InvestorBaseForm):
    def __init__(self, *args, **kwargs):
        super(InvestorForm, self).__init__(*args, **kwargs)

    name = forms.CharField(
        label='Name of Investment Organisation'
    )

    investor_focus = forms.CharField(
        widget=forms.Textarea(),
        label="Please describe the investor focus of your organisation")

    preferred_industries = forms.MultipleChoiceField(
        choices=(('agriculture', "Agriculture"),
                 ('manufacturing', "Manufacturing and Assembly"),
                 ('financial', "Financial Services"),
                 ('renewable', "Renewable Energy"),
                 ('information security', "Information Security"),
                 ('education', "Education"),
                 ('health', "Healthcare & Services"),
                 ('infrastructure', "Infrastructure"),
                 ('transport', "Transport"), ),
        widget=forms.CheckboxSelectMultiple,
        label="Please select your preferred industries",
        required=False)

    investment_stage = forms.MultipleChoiceField(
        choices=(("Concept Stage", "Concept stage"),
                 ("Seed stage (finding product market fit)", "Seed stage (finding product market fit)"),
                 ("Venture captial (growth)", "Venture captial (growth)"),
                 ("Private Equity (scaling and expansion)", "Private Equity (scaling and expansion)"), ),
        widget=forms.CheckboxSelectMultiple,
        label="At what stage do you make investments?")

    ticket_size = forms.CharField(
        label="Please tell us your ticket size for investments")

    url = forms.URLField(
        label="What is your organisational URL?",
        widget=forms.URLInput(attrs={'placeholder': "http://example.com/path/"})
    )

    logo = forms.ImageField(label='Organisational logo (jpg, png, gif)', required=False)

    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('organisation_name',
              css_class='text-small'),
        Field('investor_focus',
              css_class='text-large'),
        Field('prefered_industries',
                         css_class='input-xlarge'),
        Field('other_industries', css_class='text-small'),
        Field('investment_stage',
              css_class='input-xlarge'),
        Field('ticket_size',
              css_class='text-small'),
        Field('url',
              css_class='text-small'),
        Field('logo',
              css_class='input-xlarge'),

        FormActions(
            Button('cancel','Cancel', css_class='cancelBtn'),
            Submit(
                'next',
                'Submit',
                css_class="cancelBtn"
            )
        ),)

    class Meta:
        model = InvestmentCompany
        fields = ('name', 'investor_focus',
                  'prefered_industries', 'other_industries',
                  'investment_stage', 'ticket_size', 'url',
                  'logo')