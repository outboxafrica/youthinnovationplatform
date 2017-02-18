import re
from django.contrib.auth.models import User
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineCheckboxes
from django.core.validators import RegexValidator, URLValidator, EmailValidator, ValidationError


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    remember = forms.CharField(widget=forms.CheckboxInput, label="Remember Me")

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('email', css_class='sign_text'),
            Field('password', css_class='sign_text'),
            Field('remember'),
            Submit('login', 'Sign in', css_class='cancelBtn')
        )


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )


class RegisterForm(forms.Form):
    full_names = forms.CharField(max_length=300, required=True)
    roles = forms.ChoiceField(
        choices=(
            ('innovator', "I am an Entrepreneur/Innovator"),
            ('mentor', "I am a Mentor"),
            ('investor', "I am an Investor"),
            ('hub_manager', "Community Hub Manager"), )
    )
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('full_names', css_class='sign_text'),
            Field('roles', css_class='sign_text-real'),
            Field('email', css_class='sign_text'),
            Field('password', css_class='sign_text'),
            Field('confirm_password', css_class='sign_text'),
            Submit('register', 'Sign up', css_class='cancelBtn')
        )