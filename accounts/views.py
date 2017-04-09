from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from . import forms, models
from projects import forms as project_forms
from projects import models as project_models


class SignUpView(generic.CreateView):
    form_class = forms.SiteUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = 'accounts:login'


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.user.profile.get_absolute_url()


class LogOutView(LoginRequiredMixin, generic.RedirectView):
    url = reverse_lazy('accounts:login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        lookup = kwargs.get('slug')
        user = models.SiteUser.objects.get(username=lookup)
        profile = project_models.Profile.objects.prefetch_related('skills').get(user=user)
        context['profile'] = profile
        context['skills'] = [skill for skill in profile.skills.all()]

        return context


class EditProfileView(LoginRequiredMixin, generic.FormView):
    form_class = project_forms.ProfileEditForm
    template_name = 'accounts/profile_edit.html'
