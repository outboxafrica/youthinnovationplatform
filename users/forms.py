from __future__ import division
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineCheckboxes
from django.core.validators import RegexValidator, URLValidator, EmailValidator, ValidationError
from django.core.files.images import get_image_dimensions
from projects.validators import validate_img, validate_doc
from users.models import Mentor, Innovator, Investor, HubManager, ProgramManager
from YouthInnovPltfrm.forms import DivErrorList
from YouthInnovPltfrm.forms import BaseModelForm


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
        self.fields['picture'].label = "Profile Picture"

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
    facebook = forms.CharField(required=False,
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

    age = forms.ChoiceField(
        choices=(('18-20', "18-20"), ('21-25', "21-25"), ('26-30', "26-30"), ('31-40', "31-40"), ))
    # 18-20, 21-25, 26-30, 31-40

    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('full_names',
              css_class='text-small'),
        Field('gender'),
        Field('age',
              css_class='age_text'),
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
        Field('facebook',
              css_class='text-small'),
        Field('twitter',
              css_class='text-small'),
        Field('blog',
              css_class='text-small'),
        Field('website',
              css_class='text-small'),

        FormActions(
            HTML('<a class="cancelBtn btn btn-primary" href={% url "index:home" %}>Cancel</a>'),
            # Submit('Cancel', 'cancel', css_class="cancelBtn"),
            Submit(
                'next',
                'Save',
                css_class="cancelBtn"
            )
        ), )

    class Meta:
        model = Innovator
        fields = ('gender', 'phone', 'country', 'summary', 'picture',
                  'resume', 'linkedin', 'twitter', 'blog', 'website', 'full_names', 'age', 'facebook')


class MentorProfileForm(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super(MentorProfileForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList
        self.fields['full_names'].label = "Full names"
        self.fields['phone'].label = "Mobile contact"
        self.fields['summary'].label = "Please provide a summary about your educational, professional and" \
                                       " entrepreneurial experience"
        self.fields['picture'].label = "Profile Picture"
        self.fields['support_type'].label="Where can you support the innovations?"
        self.fields['support_stage'].label="At what stage of development can you support the innovation?"

    competencies = forms.CharField(
        widget=forms.Textarea(),
        label="What are your core competencies?"
    )

    support_type = forms.MultipleChoiceField(
        choices=(
            ('financial modelling', "Financial modelling"),
            ('business modelling', "Business modelling"),
            ('customer development', "Customer development"),
            ('legal', "Legal"),
            ('sales marketing', "Sales and Marketing"),
            ('technical support', "Technical Support"),
            ('building minimal viable product', "Building a minimum viable product"),
            ('raising funds', "Raising funds"),
            ('building a board', "Building a board"),
        ),
        widget=forms.CheckboxSelectMultiple
    )

    support_stage = forms.MultipleChoiceField(
        choices=(
            ('concept stage', "Concept stage"),
            ('seed stage (finding product market fit)', "Seed stage (finding product market fit)"),
            ('venture captial (growth)', "Venture captial (growth)"),
            ('private equity (scaling and expansion)', "Private Equity (scaling and expansion)"),
        ),
        widget=forms.CheckboxSelectMultiple
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

    facebook = forms.CharField(required=False,
                           widget=forms.URLInput(attrs={'placeholder': "http://example.com"}))
    website = forms.CharField(
        required=False,
        widget=forms.URLInput(attrs={'placeholder': "http://example.com"}))
    summary = forms.CharField(widget=forms.Textarea(attrs={'class': ""}))
    gender = forms.ChoiceField(
        choices=(('male', "Male"), ('female', "Female")),
        widget=forms.RadioSelect,
        initial='female', )

    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('full_names',
              css_class='text-small'),
        Field('gender'),
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
        Field('facebook',
              css_class='text-small'),
        Field('twitter',
              css_class='text-small'),
        Field('blog',
              css_class='text-small'),
        Field('website',
              css_class='text-small'),
        Field('competencies', css_class='text-large', rows=3),
        InlineCheckboxes('support_stage',),
        InlineCheckboxes('support_type',),

        FormActions(
            HTML('<a class="cancelBtn btn btn-primary" href={% url "index:home" %}>Cancel</a>'),
            Submit(
                'next',
                'Save',
                css_class="cancelBtn"
            )
        ), )

    class Meta:
        model = Mentor
        fields = ('gender', 'phone', 'country', 'summary', 'picture',
                  'resume', 'linkedin', 'twitter', 'blog', 'website', 'full_names', 'support_stage',
                  'support_type', 'competencies', 'facebook')


class InvestorProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InvestorProfileForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList
        self.fields['full_names'].label = "Full names"
        self.fields['phone'].label = "Mobile contact"
        self.fields['summary'].label = "Please provide a summary about your educational, professional and" \
                                       " entrepreneurial experience"
        self.fields['picture'].label = "Profile Picture"

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

    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('full_names',
              css_class='text-small'),
        Field('gender'),
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
            HTML('<a class="cancelBtn btn btn-primary" href={% url "index:home" %}>Cancel</a>'),
            Submit(
                'next',
                'Save',
                css_class="cancelBtn"
            )
        ), )

    class Meta:
        model = Investor
        fields = ('gender', 'phone', 'country', 'summary', 'picture',
                  'resume', 'linkedin', 'twitter', 'blog', 'website', 'full_names')



class HubManagerProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HubManagerProfileForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList
        self.fields['full_names'].label = "Full names"
        self.fields['phone'].label = "Mobile contact"
        self.fields['summary'].label = "Please provide a summary about your educational, professional and" \
                                       " entrepreneurial experience"
        self.fields['picture'].label = "Profile Picture"

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
            HTML('<a class="cancelBtn btn btn-primary" href={% url "index:home" %}>Cancel</a>'),
            Submit(
                'next',
                'Save',
                css_class="cancelBtn"
            )
        ), )

    class Meta:
        model = HubManager
        fields = ('gender', 'phone', 'country', 'summary', 'picture',
                  'resume', 'linkedin', 'twitter', 'blog', 'website', 'full_names', 'age')


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
    facebook = forms.CharField(required=False,
                           widget=forms.URLInput(attrs={'placeholder': "http://example.com"}))
    website = forms.CharField(
        required=False,
        widget=forms.URLInput(attrs={'placeholder': "http://example.com"}))
    summary = forms.CharField(widget=forms.Textarea(attrs={'class': ""}))
    gender = forms.ChoiceField(
        choices=(('male', "Male"), ('female', "Female")),
        widget=forms.RadioSelect,
        initial='female', )


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
        Field('facebook',
              css_class='text-small'),
        Field('twitter',
              css_class='text-small'),
        Field('blog',
              css_class='text-small'),
        Field('website',
              css_class='text-small'),

        FormActions(
            HTML('<a class="cancelBtn btn btn-primary" href={% url "index:home" %}>Cancel</a>'),
            Submit(
                'next',
                'Save',
                css_class="cancelBtn"
            )
        ), )

    class Meta:
        model = ProgramManager
        fields = ('gender', 'phone', 'country', 'summary', 'picture',
                  'resume', 'linkedin', 'twitter', 'blog', 'website', 'full_names', 'age')




class FormT(forms.Form):
    name = forms.CharField(max_length=100)
    error_css_class = 'error'
    required_css_class = 'req'
