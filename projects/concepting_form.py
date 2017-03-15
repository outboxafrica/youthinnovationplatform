from django.contrib.auth.models import User
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineCheckboxes
from projects.models import Innovation
from projects.validators import validate_img, validate_xls
from YouthInnovPltfrm.forms import BaseModelForm


class ConceptingForm1(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super(ConceptingForm1, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Idea name"
        self.fields['description'].label = "Please describe your idea"
        self.fields['sectors'].label = "What sectors do you operate in?"
        self.fields['challenge_to_solve'].label = "What problems/Challenges or needs is your idea trying to solve?"
        self.fields['challenge_faced'].label = "What challenges are you facing?"

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
    challenge_faced = forms.MultipleChoiceField(
        choices=(
            ('mentorship', "Mentorship"),
            ('office space', "Office Space"),
            ('networking', "To network"),
            ('training', "Training on how to run a business"),
            ('technical', "Technical Training"),
            ('team', "To build a team"),
            ('funding', "Funding"),
        ),
        widget=forms.CheckboxSelectMultiple,
    )
    logo = forms.ImageField(validators=[validate_img], required=False)

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
        Field('logo', css_class='file-upload'),
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
        fields = (
            'name', 'description', 'sectors', 'other_sectors', 'challenge_faced', 'challenge_to_solve', 'logo')


class ConceptingForm2(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super(ConceptingForm2, self).__init__(*args, **kwargs)
        self.fields[
            'target_customers'].label = "Who are your Target customers?"
        self.fields[
            'acquisition_plan'].label = "How do you plan to reach your target customers?"
        self.fields[
            'do_really_well'].label = "What are the things you have to do really well in order to deliver value to your customers?"
        self.fields[
            'key_resources'].label = "What key resources do you need on your team?"
        self.fields[
            'key_partners'].label = "What are the key partners that you would like to work with?"
        self.fields[
            'potential_competitors'].label = "Who are your potential competitors (or what other products/services address the same issue as yourself)?"
        self.fields[
            'business_differentiator'].label = "What differentiates your idea/business from alternative products/services?"

    target_customers = forms.CharField(widget=forms.Textarea())
    acquisition_plan = forms.CharField(widget=forms.Textarea())
    do_really_well = forms.CharField(widget=forms.Textarea())
    key_resources = forms.CharField(widget=forms.Textarea())
    key_partners = forms.CharField(widget=forms.Textarea())
    potential_competitors = forms.CharField(widget=forms.Textarea(), )
    business_differentiator = forms.CharField(widget=forms.Textarea())

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('target_customers',
              rows="3",
              css_class='form-control'),
        Field('acquisition_plan',
              rows="3",
              css_class='form-control'),
        Field('potential_competitors',
              rows="3",
              css_class='form-control'),
        Field('business_differentiator',
              rows="3",
              css_class='form-control'),
        Field('do_really_well',
              rows="3",
              css_class='form-control'),
        Field('key_resources',
              rows="3",
              css_class='form-control'),
        Field('key_partners',
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
        fields = ('target_customers', 'acquisition_plan',
                  'potential_competitors', 'business_differentiator',
                  'do_really_well', 'key_resources', 'key_partners')


class ConceptingForm3(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super(ConceptingForm3, self).__init__(*args, **kwargs)
        self.fields['revenue'].label = "How will you generate revenue?"
        self.fields['costs'].label = "What do you envision as your costs?"

    revenue = forms.CharField(widget=forms.Textarea())
    costs = forms.CharField(widget=forms.Textarea())

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('revenue',
              rows="3",
              css_class='input-length2 form-control'),
        Field('costs',
              rows="3",
              css_class='input-length2 form-control'),
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
        fields = ('revenue', 'costs')
