import hashlib
import datetime
import random

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator, URLValidator, EmailValidator, ValidationError
from django.contrib import messages
from events.models import Event
from blog.models import Post
from projects.models import Innovation
from index.forms import RegisterForm, LoginForm, UserForm
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


class Accounts(TemplateView):
    template_name = 'index/accounts.html'

    def get(self, request, *args, **kwargs):
        loginform = LoginForm()
        registerform = RegisterForm()

        return render(request, self.template_name, {'loginform': loginform, 'registerform': registerform})

    def post(self, request, *args, **kwargs):
        register_form = RegisterForm(request.POST)
        login_form = LoginForm(request.POST)
        if 'login' in request.POST:
            if login_form.is_valid():
                print 'form data valid'
                cleaned_cred = login_form.cleaned_data
                print cleaned_cred
                user = authenticate(username=cleaned_cred['email'], password=cleaned_cred['password'])
                if user:
                    if user.is_active:
                        django_login(request, user)
                        try:
                            return HttpResponseRedirect(request.GET['next'])
                        except KeyError, e:
                            print e
                        return HttpResponseRedirect('/')
                    else:
                        raise ValidationError("Please check your email and validate your account")
                else:
                    # raise ValidationError("User does not exist. Please create an account")
                    print 'incorrect login'
                    messages.error(request, 'Invalid login details')
                    return HttpResponseRedirect(reverse('index:home'))
            else:
                return render(request, self.template_name, {'loginform': login_form, 'registerform': register_form})

        elif 'register' in request.POST:
            print 'Sign Up'
            if register_form.is_valid():
                cleaned_cred = register_form.cleaned_data
                role = cleaned_cred['roles']
                email = cleaned_cred['email']
                password = cleaned_cred['password']
                confirm_password = cleaned_cred['confirm_password']
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
                        key_expires=key_expires
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
                        key_expires=key_expires
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
                        key_expires=key_expires
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
                        key_expires=key_expires
                    )
                    hub_manager_profile.set_password(password)
                    hub_manager_profile.save()

                mailer = UNDPMailer()
                mailer.sendVerification(email, activation_key,
                                        request.build_absolute_uri("/"))

                messages.success(request,
                                 'Your account has been successfully created, check you email to verify your account')
                # Add analytics hit for completed project
                return HttpResponseRedirect('/accounts')

            else:
                return render(request, self.template_name, {'loginform': login_form, 'registerform': register_form})


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
