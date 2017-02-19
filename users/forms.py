from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.core.validators import RegexValidator, URLValidator, EmailValidator, ValidationError
from projects.validators import validate_img, validate_doc
from users.models import Mentor, Innovator, Investor, HubManager, ProgramManager


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['full_names'].label = "Full names"
        self.fields['phone'].label = "Mobile contact"
        self.fields['expertise'].label = "Please provide a summary about your educational, professional and" \
                                         " entrepreneurial experience"

    full_names = forms.CharField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format:"
        " '+256 XXX XXX'. Up to 15 digits allowed.")
    phone = forms.CharField(
        validators=[phone_regex],
        widget=forms.TextInput(attrs={'class': "",
                                      'placeholder': '+256 XXX XXX'}))
    country = forms.CharField(max_length=20)
    picture = forms.ImageField(required=False, validators=[validate_img])
    resume = forms.FileField(validators=[validate_doc], required=False)
    linkedin = forms.CharField(required=False,
        widget=forms.URLInput(attrs={'placeholder': "http://example.com"}))
    twitter = forms.CharField(required=False,
        widget=forms.URLInput(attrs={'placeholder': "http://example.com"}))
    blog = forms.CharField(required=False,
        widget=forms.URLInput(attrs={'placeholder': "http://example.com"}))
    website = forms.CharField(
        required=False,
        widget=forms.URLInput(attrs={'placeholder': "http://example.com"}))
    expertise = forms.CharField(widget=forms.Textarea(attrs={'class': ""}))
    gender = forms.ChoiceField(
        choices=(('male', "Male"), ('female', "Female")),
        widget=forms.RadioSelect,
        initial='female', )

    age = forms.IntegerField(min_value=20, widget=forms.TextInput(attrs={'placeholder': '20'}))

    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('full_names',
              css_class='text-small'),
        Field('gender'),
        Field('age',
                css_class='sign_text'),
        Field('phone',
              css_class='text-small'),
        Field('country',
              css_class='text-small'),
        Field('expertise',
              rows="3",
              css_class='text-large'),
        Field('picture',
              css_class='file-upload'),
        Field('resume',
              css_class='file-upload'),
        Field('linkedin',
              css_class='text-small'),
        Field('twitter',
              css_class='text-small'),
        Field('blog',
              css_class='text-small'),
        Field('website',
              css_class='text-small'),

        FormActions(
            Button('Cancel', 'cancel', css_class="cancelBtn"),
            Submit(
                'next',
                'Next',
                css_class="cancelBtn"
            )
        ),)

    class Meta:
        model = Innovator
        fields = ('gender', 'phone', 'country', 'expertise', 'picture',
                  'resume', 'linkedin', 'twitter', 'blog', 'website', 'full_names','age')