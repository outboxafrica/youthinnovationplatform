from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.contrib.auth.decorators import login_required
from users.forms import ProfileForm
from users.models import User

# Create your views here.


class EditUser(FormView):
    form_class = ProfileForm
    template_name = 'users/edit_user.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super(EditUser, self).form_valid(form)

    def form_invalid(self, form):
        return super(EditUser, self).form_valid(form)

    def get_form(self, form_class=None):
        form_class = self.form_class
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


class ViewProfile(TemplateView):
    model = User
    template_name = 'users/my_profile.html'

    def get_context_data(self, **kwargs):
        context = super(ViewProfile, self).get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        context['userprofile'] = user
        return context


