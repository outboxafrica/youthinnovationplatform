from django import forms
from users.models import User
from crispy_forms.helper import FormHelper
from django.contrib.auth import authenticate
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from django.core.validators import ValidationError
from YouthInnovPltfrm.forms import BaseForm


class SignInForm(BaseForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
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

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     try:
    #         user = User.objects.get(email=email)
    #     except User.DoesNotExist:
    #         raise forms.ValidationError(u'This email is not registered on this platform')
    #
    #     return email

    def clean(self):
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')

        if not (password and email):
            self.add_error('email', '')
            self.add_error('password', '')
            return self.cleaned_data

        else:
            user = authenticate(username=email, password=password)
            if not user:
                print "clean not user"
                self.add_error('email', '')
                self.add_error('password', '')
                raise ValidationError("Wrong email or password combination")
            return self.cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )


class RegisterForm(BaseForm):
    full_names = forms.CharField(max_length=300, required=True)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    roles = forms.ChoiceField(
        choices=(('innovator', "I am an Entrepreneur/Innovator"), ('mentor', "I am a Mentor"),
                 ('investor', "I am an Investor"), ('hub_manager', "I am a Community Hub Manager"), ))

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('full_names', css_class='form-control'),
                css_class="form-group"
                ),
            Div(
                Field('roles', css_class='form-control in-selector'),
                css_class='form-group'
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
                 '<button class="btn sbtBtn" type="submit" id="">Sign Up</button></div>'),
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
            return email
        # raise forms.ValidationError(u'This email address is already taken')
        self.add_error('email', 'This email address is already taken')

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        passwordConfirm = data.get('confirm_password')
        msg = u"The passwords do not match."
        # print passwordConfirm
        # check if the confirm password field is not empty
        if passwordConfirm is not None and password is not None:
            if password != passwordConfirm:
                if passwordConfirm is not None:
                    self.add_error('confirm_password', msg)
                    self.add_error('password', msg)
                elif password is not None:
                    self.add_error('confirm_password', msg)
                    self.add_error('password', msg)
                # raise forms.ValidationError(u"The passwords do not match.")
        return self.cleaned_data


class ResetPasswordForm(BaseForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['email'].label = "Please enter your email address"
        self.helper.layout = Layout(
            Div(
                Field('email', css_class='form-control'),
                css_class="form-group"
            ),
            HTML('<div class="form-group" id="submitbtngrp">'
                 '<button class="btn sbtBtn" type="submit" id="">Submit</button></div>'),
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
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True)
    error_css_class = 'error'

    def __init__(self, *args, **kwargs):
        super(ConfirmPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['password'].label = "New password"
        self.fields['confirm_password'].label = "Retype new password"
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
                 '<button class="btn sbtBtn" type="submit" id="">Save</button></div>'),
        )

    class Meta:
        model = User
        fields = ('password',)

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        msg = u"The passwords do not match."
        if password != confirm_password:
            self.add_error('confirm_password', msg)
            self.add_error('password', msg)
        return self.cleaned_data




