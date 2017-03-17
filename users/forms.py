from __future__ import division
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.core.validators import RegexValidator, URLValidator, EmailValidator, ValidationError
from django.core.files.images import get_image_dimensions
from projects.validators import validate_img, validate_doc
from users.models import Mentor, Innovator, Investor, HubManager, ProgramManager
from YouthInnovPltfrm.forms import DivErrorList


class BaseForm(forms.ModelForm):
    def clean_picture(self):
        image = self.cleaned_data.get('picture')
        return image


class InnovatorProfileForm(BaseForm):
    def __init__(self, *args, **kwargs):
        super(InnovatorProfileForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList
        self.fields['full_names'].label = "Full names"
        self.fields['phone'].label = "Mobile contact"
        self.fields['summary'].label = "Please provide a summary about your educational, professional and" \
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
    summary = forms.CharField(widget=forms.Textarea(attrs={'class': ""}))
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
        Field('summary',
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
        ), )

    class Meta:
        model = Innovator
        fields = ('gender', 'phone', 'country', 'summary', 'picture',
                  'resume', 'linkedin', 'twitter', 'blog', 'website', 'full_names', 'age')


class MentorProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MentorProfileForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList
        self.fields['full_names'].label = "Full names"
        self.fields['phone'].label = "Mobile contact"
        self.fields['summary'].label = "Please provide a summary about your educational, professional and" \
                                       " entrepreneurial experience"
        competencies = forms.CharField(
            widget=forms.Textarea(),
            label="What are your core competencies?"
        )

        specialities = forms.MultipleChoiceField(
            choices=(
                ('financial_modelling', "Financial modelling"),
                ('business_modelling', "Business modelling"),
                ('customer_development', "Customer development"),
                ('legal', "Legal"),
                ('sales_marketing', "Sales and Marketing"),
                ('tech_support', "Technical Support"),
                ('mvp', "Building a minimum viable product"),
                ('fund_raising', "Raising funds"),
                ('board', "Building a board"),
            ),
            widget=forms.CheckboxSelectMultiple,
            label="Where can you support the innovations?"
        )

        support_stage = forms.MultipleChoiceField(
            choices=(
                ('concept_stage', "Concept stage"),
                ('seed_stage', "Seed stage (finding product market fit)"),
                ('venture_capital', "Venture captial (growth)"),
                ('private_equity', "Private Equity (scaling and expansion)"),
            ),
            widget=forms.CheckboxSelectMultiple,
            label="At what stage of development can you support the innovation?"
        )

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
    summary = forms.CharField(widget=forms.Textarea(attrs={'class': ""}))
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
        Field('summary',
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
        Field('competencies', css_class='text-large', rows=4),
        Field('specialities', css_class='input-xlarge'),
        Field('support_stage', css_class='input-xlarge'),

        FormActions(
            Button('Cancel', 'cancel', css_class="cancelBtn"),
            Submit(
                'next',
                'Next',
                css_class="cancelBtn"
            )
        ), )

    class Meta:
        model = Mentor
        fields = ('gender', 'phone', 'country', 'summary', 'picture',
                  'resume', 'linkedin', 'twitter', 'blog', 'website', 'full_names', 'age', 'support_stage',
                  'support_type', 'competencies')

    def clean_picture(self):
        image = self.cleaned_data.get('picture', False)
        w, h = get_image_dimensions(image)
        aspect_ratio = w/h
        if image:
            if image._size > 4 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 4mb )")
            elif aspect_ratio != 1:
                raise ValidationError("Image must have an aspect ratio of 1:1")
            return image
        else:
            raise ValidationError("Image file can not be read")


class InvestorProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InvestorProfileForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList
        self.fields['full_names'].label = "Full names"
        self.fields['phone'].label = "Mobile contact"
        self.fields['summary'].label = "Please provide a summary about your educational, professional and" \
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
    summary = forms.CharField(widget=forms.Textarea(attrs={'class': ""}))
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
        Field('summary',
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
        ), )

    class Meta:
        model = Investor
        fields = ('gender', 'phone', 'country', 'summary', 'picture',
                  'resume', 'linkedin', 'twitter', 'blog', 'website', 'full_names', 'age')

    def clean_picture(self):
        image = self.cleaned_data.get('picture', False)
        w, h = get_image_dimensions(image)
        aspect_ratio = w/h
        if image:
            if aspect_ratio != 1:
                raise ValidationError("Image must have an aspect ratio of 1:1")
            return image
        else:
            raise ValidationError("Image file can not be read")


class HubManagerProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HubManagerProfileForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList
        self.fields['full_names'].label = "Full names"
        self.fields['phone'].label = "Mobile contact"
        self.fields['summary'].label = "Please provide a summary about your educational, professional and" \
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
    summary = forms.CharField(widget=forms.Textarea(attrs={'class': ""}))
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
        Field('summary',
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
        ), )

    class Meta:
        model = HubManager
        fields = ('gender', 'phone', 'country', 'summary', 'picture',
                  'resume', 'linkedin', 'twitter', 'blog', 'website', 'full_names', 'age')

    def clean_picture(self):
        image = self.cleaned_data.get('picture')
        w, h = get_image_dimensions(image)
        aspect_ratio = w/h
        if image:
            if aspect_ratio != 1:
                raise ValidationError("Image must have an aspect ratio of 1:1")
            return image
        else:
            raise ValidationError("Image file can not be read")


class ProgramManagerProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProgramManagerProfileForm, self).__init__(*args, **kwargs)
        self.fields['full_names'].label = "Full names"
        self.fields['phone'].label = "Mobile contact"
        self.fields['summary'].label = "Please provide a summary about your educational, professional and" \
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
    summary = forms.CharField(widget=forms.Textarea(attrs={'class': ""}))
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
        ), )

    class Meta:
        model = ProgramManager
        fields = ('gender', 'phone', 'country', 'summary', 'picture',
                  'resume', 'linkedin', 'twitter', 'blog', 'website', 'full_names', 'age')

    def clean_picture(self):
        image = self.cleaned_data.get('image', False)
        w, h = get_image_dimensions(image)
        aspect_ratio = w/h
        if image:
            if aspect_ratio != 1:
                raise ValidationError("Image must have an aspect ratio of 1:1")
            return image
        else:
            raise ValidationError("Image file can not be read")


class FormT(forms.Form):
    name = forms.CharField(max_length=100)
    error_css_class = 'error'
    required_css_class = 'req'
