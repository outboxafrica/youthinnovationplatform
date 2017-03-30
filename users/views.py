from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView, TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.forms import InnovatorProfileForm, InvestorProfileForm, MentorProfileForm, HubManagerProfileForm, ProgramManagerProfileForm
from users.models import User, Mentor, Innovator, Investor, HubManager, ProgramManager

# Create your views here.


class EditUser(FormView):
    template_name = 'users/edit_user.html'
    success_url = 'view'

    def get_form_class(self):
        role = self.request.user.role
        if role == 'mentor':
            form_class = MentorProfileForm
        elif role == 'innovator':
            print 'innovator form'
            form_class = InnovatorProfileForm
        elif role == 'investor':
            print 'investor form'
            form_class = InvestorProfileForm
        elif role == 'hub manager':
            form_class = HubManagerProfileForm
        elif role == 'program manager':
            form_class = ProgramManagerProfileForm

        return form_class

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super(EditUser, self).form_valid(form)

    def form_invalid(self, form):
        return super(EditUser, self).form_invalid(form)

    def get_form(self, form_class=None):
        form_class = self.get_form_class()
        try:
            user = User.objects.get(pk=self.request.user.id)
            print type(user)
            user.full_name = user.get_full_name()
            return form_class(instance=user, **self.get_form_kwargs())
        except User.DoesNotExist:
            return form_class(**self.get_form_kwargs())

    def get_initial(self):
        initial = super(EditUser, self).get_initial()
        try:
            user = User.objects.get(pk=self.request.user.id)
            initial['full_names'] = user.get_full_name()
            return initial
        except User.DoesNotExist:
            return initial

    def get_context_data(self, **kwargs):
        context = super(EditUser, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        context['userprofile'] = user
        return context


class ViewProfile(TemplateView):
    model = User
    template_name = 'users/my_profile.html'

    def get_context_data(self, **kwargs):
        context = super(ViewProfile, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        context['userprofile'] = user
        print user.picture
        print user.role
        return context


def view_profile(request):
    # user = User.objects.get(pk=request.user.id)
    # return render(request, 'users/my_profile.html', {'userprofile': user})
    user = User.objects.get(pk=request.user.id)

    if not request.user.has_created_entity:
        if request.user.gender:
            return render(request, 'users/my_profile.html', {'userprofile': user})
        else:
            return HttpResponseRedirect(reverse('projects:select-startup-stage'))
    else:
        return render(request, 'users/my_profile.html', {'userprofile': user})