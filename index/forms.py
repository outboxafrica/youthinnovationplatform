import re
from django import forms
from users.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from django.core.validators import RegexValidator, URLValidator, EmailValidator, ValidationError


class SignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    remember = forms.CharField(widget=forms.CheckboxInput, label="Remember Me", required=False)

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('email', css_class='form-control'),
                css_class="form-group"
            ),

            Div(
                Field('password', css_class='form-control'),
                HTML('<a href="{% url "index:password" %}" class="float-right">Forgot your password?</a>'),
                css_class="form-group"
            ),
            Div(
                HTML('<label><input type="checkbox">Keep me signed in</label>'),
                css_class='checkbox'
            ),
            HTML('<div class="form-group" id="submitbtngrp">'
                 '<button class="btn sbtBtn" type="submit" id="">Sign in</button></div>'),

            HTML('<a href="{% url "index:register" %}">Create an account?</a>'),

        )


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )


class RegisterForm(forms.Form):
    full_names = forms.CharField(max_length=300, required=True)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('full_names', css_class='form-control'),
                css_class="form-group"
                ),
            HTML(
                '<div class="form-group"><label class="control-label">Role </label>'
                '<select class="form-control" name="roles">'
                '<optgroup label="Select a role">'
                '<option value="innovator">Innovator</option>'
                '<option value="investor">Investor</option>'
                '<option value="mentor">Mentor</option>'
                '<option value="hub_manager">Hub Manager</option>'
                '</optgroup></select></div>'
            ),
            Div(
                Field('email', css_class='form-control'),
                css_class="form-group"
            ),
            Div(
                Field('password', css_class='form-control'),
                css_class="form-group"
            ),
            Div(
                Field('confirm_password', css_class='form-control'),
                css_class="form-group"
            ),
            HTML('<div class="form-group" id="submitbtngrp">'
                 '<button class="btn sbtBtn" type="submit" id="">Sign in</button></div>'),
            HTML('<a href="{% url "index:signin" %}">Already have an account? Sign in</a>'),

            # Field('full_names', css_class='sign_text'),
            # Field('roles', css_class='sign_text-real'),
            # Field('email', css_class='sign_text'),
            # Field('password', css_class='sign_text'),
            # Field('confirm_password', css_class='sign_text'),
            # Submit('register', 'Sign up', css_class='cancelBtn', css_id='submitbtn')
        )

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError(u'This email address is already taken')
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        passwordConfirm = data.get('confirm_password')
        if password != passwordConfirm:
            raise forms.ValidationError(u"The passwords do not match.")
        return self.cleaned_data


class ResetPasswordForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('email', css_class='form-control'),
                css_class="form-group"
            ),
            HTML('<div class="form-group" id="submitbtngrp">'
                 '<button class="btn sbtBtn" type="submit" id="">Send reset link</button></div>'),
        )

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            print user
        except User.DoesNotExist:
            raise forms.ValidationError(u'This email address is not registered')
        return email


class ConfirmPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(ConfirmPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('password', css_class='form-control'),
                css_class="form-group"
            ),
            Div(
                Field('confirm_password', css_class='form-control'),
                css_class="form-group"
            ),
            HTML('<div class="form-group" id="submitbtngrp">'
                 '<button class="btn sbtBtn" type="submit" id="">Reset Password</button></div>'),
        )

    class Meta:
        model = User
        fields = ('password',)

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise ValidationError(u"The passwords do not match.")
        return self.cleaned_data




