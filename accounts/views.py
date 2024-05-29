from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView
from .models import CustomUser
from .forms import ProfileForm  # Ensure this import is correct

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

class ProfileEditView(UpdateView):
    model = CustomUser
    form_class = ProfileForm
    template_name = 'accounts/profile_form.html'
    success_url = '/accounts/profile/'

    def get_object(self):
        return self.request.user


