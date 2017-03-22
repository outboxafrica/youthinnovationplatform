from django.contrib.auth.models import User
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineCheckboxes
from projects.models import Innovation
from projects.validators import validate_img, validate_xls
from YouthInnovPltfrm.forms import BaseModelForm


class ValidationForm1(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super(ValidationForm1, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Idea name"
        self.fields['description'].label = "Please describe your idea"
        self.fields[
            'url'].label = "Please share a url to the website with your product"
        self.fields['sectors'].label = "What sectors do you operate in?"
        self.fields[
            'challenge_to_solve'].label = "What problems/Challenges or needs is your idea trying to solve?"
        self.fields[
            'challenge_faced'].label = "What challenges are you facing?"
        self.fields[
            'service_pic'].label = "Please provide a picture that shows yrour product/service (jpeg, png, gif)"
        self.fields[
            'service_videos'].label = "Please provide a link to the video that shows your product/service. " \
                                      "[This can be a link to youtube or vimeo]"

    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    url = forms.CharField()
    service_pic = forms.ImageField(required=False)
    service_videos = forms.CharField()
    sectors = forms.MultipleChoiceField(
        choices=(('agriculture', "Agriculture"),
                 ('manufacturing', "Manufacturing and Assembly"),
                 ('financial', "Financial Services"),
                 ('renewable', "Renewable Energy"),
                 ('infosec', "Information Security"),
                 ('education', "Education"),
                 ('health', "Healthcare & Services"),
                 ('infrastructure', "Infrastructure"),
                 ('transport', "Transport"), ),
        widget=forms.CheckboxSelectMultiple, )
    challenge_to_solve = forms.CharField(widget=forms.Textarea())
    challenge_faced = forms.MultipleChoiceField(
        choices=(('mentorship', "Mentorship"),
                 ('office', "Office Space"),
                 ('networking', "To network"),
                 ('training', "Training on how to run a business"),
                 ('technical', "Technical Training"),
                 ('team', "To build a team"),
                 ('funding', "Funding"),
                 ('office', "Office Space"), ),
        widget=forms.CheckboxSelectMultiple, )
    logo = forms.ImageField(validators=[validate_img], required=False)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('name',
              css_class='input-length3 form-control'),
        Field('description',
              rows="3",
              css_class='input-length3 form-control'),
        Field('url',
              css_class='input-length3 form-control'),
        Field('service_pic',
              css_class='file-upload'),
        Field('service_videos',
              css_class='input-length3 form-control'),
        InlineCheckboxes('sectors'),
        Field('other_sectors',
              css_class='input-length3 form-control'),
        Field('challenge_to_solve',
              rows="3",
              css_class='input-length3 form-control'),
        InlineCheckboxes('challenge_faced',),
        Field('logo',
              css_class='file-upload'),
        FormActions(
            Submit('validation_form_1', 'Next', css_class="cancelBtn btnNext"),
        )
    )

    class Meta:
        model = Innovation
        fields = ('name', 'description', 'url', 'sectors', 'other_sectors', 'challenge_faced',
                  'challenge_to_solve', 'logo', 'service_pic',
                  'service_videos')


class ValidationForm2(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super(ValidationForm2, self).__init__(*args, **kwargs)
        self.fields[
            'target_customers'].label = "Who are your Target customers?"
        self.fields[
            'problem_change'].label = "Has the problem/need changed ever since you started testing with your customers?"
        self.fields[
            'customer_change'].label = "Have your customers changed every since you tried testing with them?"
        self.fields[
            'customer_lessons'].label = "What did you learn on how to reach your customers?"
        self.fields[
            'planned_acquisition_plan'].label = "At the idea conception, how did you plan to reach your customers?"
        self.fields[
            'acquisition_plan'].label = "How do you plan to reach and acquire your target customers?"
        self.fields[
            'test_plan'].label = "How did or are you currently testing with your customers?"
        self.fields[
            'performance'].label = "Please share share some figures on how your product has performed while testing " \
                                   "with actual users"
        self.fields[
            'test_learnings'].label = "Can you please share your biggest learnings after testing your product with " \
                                      "customers?"
        self.fields[
            'potential_competitors'].label = "Who are your potential competitors (or what other products/services " \
                                             "address the same issue as yourself)?"
        self.fields[
            'business_differentiator'].label = "What differentiates your idea/business from alternative " \
                                               "products/services?"

    target_customers = forms.CharField(widget=forms.Textarea())
    problem_change = forms.CharField(widget=forms.Textarea())
    customer_change = forms.CharField(widget=forms.Textarea())
    customer_lessons = forms.CharField(widget=forms.Textarea())
    planned_acquisition_plan = forms.CharField(widget=forms.Textarea())
    acquisition_plan = forms.CharField(widget=forms.Textarea())
    test_plan = forms.CharField(widget=forms.Textarea())
    performance = forms.CharField(widget=forms.Textarea())
    test_learnings = forms.CharField(widget=forms.Textarea())
    potential_competitors = forms.CharField(widget=forms.Textarea())
    business_differentiator = forms.CharField(widget=forms.Textarea())

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('target_customers',
              rows='3',
              css_class='form-control'),
        Field('problem_change',
              rows='3',
              css_class='form-control'),
        Field('customer_change',
              rows='3',
              css_class='form-control'),
        Field('customer_lessons',
              rows='3',
              css_class='form-control'),
        Field('planned_acquisition_plan',
              rows='3',
              css_class='form-control'),
        Field('acquisition_plan',
              rows='3',
              css_class='form-control'),
        Field('test_plan',
              rows='3',
              css_class='form-control'),
        Field('performance',
              rows='3',
              css_class='form-control'),
        Field('test_learnings',
              rows='3',
              css_class='form-control'),
        Field('potential_competitors',
              rows='3',
              css_class='form-control'),
        Field('business_differentiator',
              rows='3',
              css_class='form-control'),
        FormActions(
            Button('Cancel', 'Previous', css_class="cancelBtn btnPrevious"),
            Submit('validation_form_2', 'Next', css_class="cancelBtn btnNext"),
        )
    )

    class Meta:
        model = Innovation
        fields = ('target_customers', 'problem_change', 'customer_change',
                  'customer_lessons', 'planned_acquisition_plan',
                  'acquisition_plan', 'test_plan', 'performance',
                  'test_learnings', 'potential_competitors',
                  'business_differentiator')


class ValidationForm3(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super(ValidationForm3, self).__init__(*args, **kwargs)
        self.fields['revenue'].label = "How will you generate revenue?"
        self.fields['costs'].label = "What do you envision as your costs?"

    revenue = forms.CharField(widget=forms.Textarea(), )

    costs = forms.CharField(widget=forms.Textarea(), )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('revenue',
              rows="3",
              css_class='input-length2 form-control'),
        Field('costs',
              rows="3",
              css_class='input-length2 form-control'),
        FormActions(
            Submit('validation_form_3', 'Finish', css_class="cancelBtn btnNext"),
        )
    )

    class Meta:
        model = Innovation
        fields = ('revenue', 'costs')
