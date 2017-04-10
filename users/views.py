from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView, TemplateView, UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.forms import InnovatorProfileForm, InvestorProfileForm, MentorProfileForm, HubManagerProfileForm, ProgramManagerProfileForm
from users.models import User, Mentor, Innovator, Investor, HubManager, ProgramManager

# Create your views here.


class EditMentor(UpdateView):
    form_class = MentorProfileForm
    model = Mentor
    template_name = 'users/edit_user.html'
    success_url = '/users/view'

    def form_invalid(self, form):
        return super(EditMentor, self).form_invalid(form)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super(EditMentor, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EditMentor, self).get_context_data(**kwargs)
        mentor = Mentor.objects.get(pk=self.request.user.id)
        context['userprofile'] = mentor
        return context

    def get_initial(self):
        initial = super(EditMentor, self).get_initial()
        try:
            user = User.objects.get(pk=self.request.user.id)
            initial['full_names'] = user.get_full_name()
            return initial
        except User.DoesNotExist:
            return initial


class EditInvestor(UpdateView):
    form_class = InvestorProfileForm
    model = Investor
    template_name = 'users/edit_user.html'
    success_url = 'view'

    def form_invalid(self, form):
        return super(EditInvestor, self).form_invalid(form)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super(EditInvestor, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EditInvestor, self).get_context_data(**kwargs)
        investor = Investor.objects.get(pk=self.request.user.id)
        context['userprofile'] = investor
        return context

    def get_initial(self):
        initial = super(EditInvestor, self).get_initial()
        try:
            user = User.objects.get(pk=self.request.user.id)
            initial['full_names'] = user.get_full_name()
            return initial
        except User.DoesNotExist:
            return initial


class EditHubManager(UpdateView):
    form_class = HubManagerProfileForm
    template_name = 'users/edit_user.html'
    success_url = 'view'
    model = HubManager

    def form_invalid(self, form):
        return super(EditHubManager, self).form_invalid(form)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super(EditHubManager, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EditHubManager, self).get_context_data(**kwargs)
        hub_manager = HubManager.objects.get(pk=self.request.user.id)
        context['userprofile'] = hub_manager
        return context

    def get_initial(self):
        initial = super(EditHubManager, self).get_initial()
        try:
            user = User.objects.get(pk=self.request.user.id)
            initial['full_names'] = user.get_full_name()
            return initial
        except User.DoesNotExist:
            return initial


class EditInnovator(UpdateView):
    form_class = InnovatorProfileForm
    template_name = 'users/edit_user.html'
    success_url = 'view'
    model = Innovator

    def form_invalid(self, form):
        return super(EditInnovator, self).form_invalid(form)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super(EditInnovator, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EditInnovator, self).get_context_data(**kwargs)
        innovator = Innovator.objects.get(pk=self.request.user.id)
        context['userprofile'] = innovator
        return context

    def get_initial(self):
        initial = super(EditInnovator, self).get_initial()
        try:
            user = User.objects.get(pk=self.request.user.id)
            initial['full_names'] = user.get_full_name()
            return initial
        except User.DoesNotExist:
            return initial


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
    if user.role == 'mentor':
        mentor = Mentor.objects.get(pk=request.user.id)
        return render(request, 'users/my_profile.html', {'userprofile': mentor})
    elif user.role == 'innovator':
        innovator = Innovator.objects.get(pk=request.user.id)
        return render(request, 'users/my_profile.html', {'userprofile': innovator})
    else:
        return render(request, 'users/my_profile.html', {'userprofile': user})
