from django.contrib.auth.models import User
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineCheckboxes
from projects.models import Innovation
from projects.validators import validate_img, validate_xls
from YouthInnovPltfrm.forms import BaseModelForm


class CommitmentForm1(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super(CommitmentForm1, self).__init__(*args, **kwargs)
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
            'challenge_to_solve'].label = "What challenges or need is your idea trying to solve?"
        self.fields[
            'challenge_faced'].label = "What challenges are you facing?"
        self.fields['other_challenges'].label = ""

    name = forms.CharField()
    logo = forms.ImageField(validators=[validate_img], required=False)
    service_pic = forms.ImageField(required=True)
    service_videos = forms.URLField(required=False)
    url = forms.URLField(required=False)
    description = forms.CharField(widget=forms.Textarea(), )
    sectors = forms.MultipleChoiceField(
        required=True,
        choices=(('agriculture', "Agriculture"),
                 ('manufacturing', "Manufacturing and Assembly"),
                 ('financial', "Financial Services"),
                 ('renewable', "Renewable Energy"),
                 ('infosec', "Information Security"),
                 ('education', "Education"),
                 ('health', "Healthcare & Services"),
                 ('infrastructure', "Infrastructure"),
                 ('transport', "Transport"),),
        widget=forms.CheckboxSelectMultiple,
    )

    challenge_to_solve = forms.CharField(widget=forms.Textarea(),)

    challenge_faced = forms.MultipleChoiceField(
        choices=(
            ('mentorship', "Mentorship"),
            ('office', "Office Space"),
            ('networking', "To network"),
            ('training', "Training on how to run a business"),
            ('technical', "Technical Training"),
            ('team', "To build a team"),
            ('funding', "Funding"),
            ('office', "Office Space"),
            ('others', "Others"),
        ),
        widget=forms.CheckboxSelectMultiple, )
    other_sectors = forms.CharField(required=False, max_length=2000)
    other_challenges = forms.CharField(widget=forms.Textarea(), required=False)
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('name',
              css_class='input-length3 form-control text-small'),
        Field('description',
              rows="3",
              css_class='input-length3 form-control text-large'),
        Field('url',
              css_class='input-length3 form-control text-small', placeholder='https://innovation.com'),
        Field('service_pic',
              css_class='file-upload'),
        Field('service_videos',
              css_class='input-length3 form-control text-small',
              placeholder='https://www.youtube.com/watch?v=eedeXTWZUn8'),
        InlineCheckboxes('sectors'),
        Field('other_sectors',
              css_class='text-small'),
        Field('challenge_to_solve',
              rows="3",
              css_class='input-length3 form-control text-large'),
        InlineCheckboxes('challenge_faced', ),
        Field('other_challenges', css_class='text-small', placeholder="Other Challenges"),
        Field('logo',
              css_class='file-upload'),
        FormActions(
            HTML('<a class="cancelBtn btn btn-primary" href={% url "index:home" %}>Cancel</a>'),
            Submit('commitment_form_1', 'Next', css_class="cancelBtn btnNext"),
        )
    )

    class Meta:
        model = Innovation
        fields = ('name', 'description', 'url', 'sectors', 'other_sectors', 'challenge_faced',
                  'challenge_to_solve', 'logo', 'service_pic', 'other_challenges',
                  'service_videos')


class CommitmentForm2(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super(CommitmentForm2, self).__init__(*args, **kwargs)
        self.fields['target_customers'].label = "Who are your Target customers?"
        self.fields['acquisition_plan'].label = "How do you plan to reach and acquire your target customers?"
        self.fields[
            'test_plan'].label = "How do you plan to test for your first product/service release with your customers?"
        self.fields[
            'impact_measure_plan'].label = "How will you measure the impact of your first product/service release with your customers?"
        self.fields[
            'show_success_plan'].label = "What will show you that after testing your product with your customers, that it was success?"
        self.fields[
            'potential_competitors'].label = "Who are your potential competitors (or what other products/services address the same issue as yourself)?"
        self.fields[
            'business_differentiator'].label = "What differentiates your idea/business from alternative products/services?"

    target_customers = forms.CharField(widget=forms.Textarea())
    acquisition_plan = forms.CharField(widget=forms.Textarea())
    test_plan = forms.CharField( widget=forms.Textarea())
    impact_measure_plan = forms.CharField(widget=forms.Textarea())
    show_success_plan = forms.CharField(widget=forms.Textarea())
    potential_competitors = forms.CharField(widget=forms.Textarea())
    business_differentiator = forms.CharField(widget=forms.Textarea())

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('target_customers', rows='3', css_class='text-large'),
        Field('acquisition_plan', rows='3', css_class='text-large'),
        Field('test_plan', rows='3', css_class='text-large'),
        Field('impact_measure_plan', rows='3', css_class='text-large'),
        Field('show_success_plan', rows='3', css_class='text-large'),
        Field('potential_competitors', rows='3', css_class='text-large'),
        Field('business_differentiator', rows='3', css_class='text-large'),
        FormActions(
            Button('cancel', 'Previous', css_class='btn-primary cancelBtn btn btnPrevious'),
            Submit('commitment_form_2', 'Next', css_class="cancelBtn btnNext"),
        )
        ,
    )

    class Meta:
        model = Innovation
        fields = ('target_customers', 'acquisition_plan', 'test_plan', 'impact_measure_plan', 'show_success_plan',
                  'potential_competitors', 'business_differentiator')


class CommitmentForm3(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommitmentForm3, self).__init__(*args, **kwargs)
        self.fields['revenue'].label = "How will you generate revenue?"
        self.fields['costs'].label = "What do you envision as your costs?"

    revenue = forms.CharField(widget=forms.Textarea())
    costs = forms.CharField(widget=forms.Textarea())

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('revenue',
              css_class='input-length2 form-control text-small'),
        Field('costs',
              css_class='input-length2 form-control text-small'),
        Button('cancel', 'Previous', css_class='btn-primary cancelBtn btn btnPrevious', onclick="window.history.back()"),
        Submit('commitment_form_3', 'Finish', css_class="cancelBtn btnNext"),
    )

    class Meta:
        model = Innovation
        fields = ('revenue', 'costs')


