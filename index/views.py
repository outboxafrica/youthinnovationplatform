import hashlib
import datetime
import random

from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator, URLValidator, EmailValidator, ValidationError
from django.contrib import messages
from events.models import Event
from blog.models import Post
from projects.models import Innovation
from index.forms import RegisterForm, LoginForm, UserForm
from index.mailer import UNDPMailer
from users.models import Innovator, Investor, HubManager, ProgramManager, Mentor

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.for_period(from_date=timezone.now())
        context['innovations'] = Innovation.objects.all().order_by("-id")[:4]
        context['blog_posts'] = Post.objects.all()[:3]
        return context


def index(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            print 'Login'
            form = LoginForm(request.POST)
            if form.is_valid():
                print 'form data valid'
                cleaned_cred = form.cleaned_data
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
                    return HttpResponseRedirect(reverse('users:index'))

        elif 'register' in request.POST:
            print 'Sign Up'
            form = RegisterForm(request.POST)
            if form.is_valid():
                cleaned_cred = form.cleaned_data
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
                user_form = UserForm(
                    data={"first_name":firstname,
                          "last_name":lastname,
                          "email": email,
                          "password": password,
                          "activation_key":activation_key,
                          "key_expires":key_expires})

                user = user_form.save(commit=False)
                user.set_password(user.password)
                user.first_name = firstname
                user.last_name = lastname
                user.is_active = False
                user.activation_key = activation_key
                user.key_expires = key_expires
                user.save()

                # Create user profile
                if role == 'innovator':
                    innovator_profile = Innovator(user=user)
                    innovator_profile.save()
                elif role == 'investor':
                    investor_profile = Investor(user=user)
                    investor_profile.save()
                elif role == 'mentor':
                    mentor_profile = Mentor(user=user)
                    mentor_profile.save()
                elif role == 'hub_manager':
                    hub_manager_profile = HubManager(user=user)
                    hub_manager_profile.save()

                mailer = UNDPMailer()
                mailer.sendVerification(email, activation_key,
                                        request.build_absolute_uri("/"))

                messages.success(request,
                                 'Your account has been successfully created')
                # Add analytics hit for completed project
                return HttpResponseRedirect('/users/verify')
            else:
                print "not valid"
                print form.errors

    loginform = LoginForm()
    registerform = RegisterForm()
    return render(request, 'index/accounts.html', {'loginform':loginform, 'registerform': registerform})
