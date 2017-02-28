import hashlib
import datetime
import random

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, FormView, DetailView
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator, URLValidator, EmailValidator, ValidationError
from django.contrib import messages
from axes.decorators import watch_login
from events.models import Event
from blog.models import Post
from projects.models import Innovation
from index.forms import RegisterForm, UserForm, ResetPasswordForm, ConfirmPasswordForm, SignInForm
from index.mailer import UNDPMailer
from users.models import Innovator, Investor, HubManager, ProgramManager, Mentor, User

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.for_period(from_date=timezone.now())
        context['innovations'] = Innovation.objects.all().order_by("-id")[:4]
        context['blog_posts'] = Post.objects.all()[:3]
        return context


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            cleaned_cred = register_form.cleaned_data
            print cleaned_cred
            role = cleaned_cred['roles']
            email = cleaned_cred['email']
            password = cleaned_cred['password']
            full_names = cleaned_cred['full_names']

            firstname = full_names.split(" ")[0]
            lastname = " ".join(full_names.split(" ")[1:])

            # generate verification code
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            activation_key = hashlib.sha1(salt + email).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(hours=24)

            # this form creates a generic user object

            # Create user profile
            if role == 'innovator':
                innovator_profile = Innovator(
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    username=email,
                    activation_key=activation_key,
                    key_expires=key_expires,
                    role='innovator',
                )
                innovator_profile.set_password(password)
                innovator_profile.save()
            elif role == 'investor':
                investor_profile = Investor(
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    username=email,
                    activation_key=activation_key,
                    key_expires=key_expires,
                    role='investor',
                )
                investor_profile.set_password(password)
                investor_profile.save()
            elif role == 'mentor':
                mentor_profile = Mentor(
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    username=email,
                    activation_key=activation_key,
                    key_expires=key_expires,
                    role='mentor',
                )
                mentor_profile.set_password(password)
                mentor_profile.save()
            elif role == 'hub_manager':
                hub_manager_profile = HubManager(
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    username=email,
                    activation_key=activation_key,
                    key_expires=key_expires,
                    role='hub_manager',
                )
                hub_manager_profile.set_password(password)
                hub_manager_profile.save()

            mailer = UNDPMailer()
            mailer.sendVerification(email, activation_key,
                                    request.build_absolute_uri("/"))

            messages.success(request,
                             'Your account has been successfully created, check you email to verify your account')
            # Add analytics hit for completed project
            return HttpResponseRedirect('/signin')

        else:
            return render(request, 'index/register.html', {'registerform': register_form})
    else:
        register_form = RegisterForm()
        return render(request, 'index/register.html', {'registerform': register_form})


def verify(request):
    return render(request, 'index/confirm.html')


def verify_key(request, key):
    user = get_object_or_404(User, activation_key=key)
    if user.key_expires < timezone.now():
        return render(request, 'index/confirm_expired.html')
    user.is_active = True
    user.save()
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    django_login(request, user)
    return render(request, 'index/confirm.html')


def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')


class ResetPasswordView(FormView):
    form_class = ResetPasswordForm
    template_name = 'index/reset_password.html'
    success_url = 'home.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form':self.form_class})

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        # generate verification code
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        activation_key = hashlib.sha1(salt + email).hexdigest()
        key_expires = datetime.datetime.today() + datetime.timedelta(hours=24)

        user = get_object_or_404(User, email=email)
        user.activation_key = activation_key
        user.key_expires = key_expires
        user.save()

        mailer = UNDPMailer()
        mailer.sendResetEmail(email, activation_key, self.request.build_absolute_uri("/"))

        return super(ResetPasswordView, self).form_valid(form)

    def form_invalid(self, form):
        return super(ResetPasswordView, self).form_invalid(form)


def confirm_password(request, key):
    form = ConfirmPasswordForm(request.POST)
    user = get_object_or_404(User, activation_key=key)
    if user.key_expires < timezone.now():
        if request.method == 'POST':
            form = ConfirmPasswordForm(request.POST)
            if form.is_valid():
                cleaned_cred = form.cleaned_data
                password = cleaned_cred['password']
                user.set_password(password)
                user.save()
                return HttpResponseRedirect(reverse('index:signin'))
            else:
                return render(request, 'index/confirm_password.html', {'form': form})
        else:
            form = ConfirmPasswordForm()
            return render(request, 'index/confirm_password.html', {'form': form})
    else:
        return render(request, 'index/confirm_expired.html')


@watch_login
def signin(request):
    login_form = SignInForm()
    if request.method == 'POST':
        login_form = SignInForm(request.POST)
        if login_form.is_valid():
            print 'form data valid'
            cleaned_cred = login_form.cleaned_data
            print cleaned_cred
            user = authenticate(username=cleaned_cred['email'], password=cleaned_cred['password'])
            if user:
                if user.is_active:
                    django_login(request, user)
                    # try:
                    #     return HttpResponseRedirect(reverse('index:home'))
                    # except KeyError, e:
                    #     print e
                    return render(request, 'index/index.html')
                else:
                    raise ValidationError("Please check your email and validate your account")
            else:
                # raise ValidationError("User does not exist. Please create an account")
                print 'incorrect login'
                messages.error(request, 'Invalid login details')
                return HttpResponseRedirect(reverse('index:signin'))
        else:
            return render(request, 'index/signin.html', {'form': login_form})
    else:
        return render(request, 'index/signin.html', {'form': login_form})

