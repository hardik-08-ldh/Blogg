from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import views
from django.urls import reverse_lazy
from members import forms
# Create your views here.
class UpdatePasswordView(views.PasswordChangeView):
    # form_class=PasswordChangeForm
    form_class=forms.PasswordUpdationForm
    success_url=reverse_lazy('home')

class UserRegisterView(CreateView):
    form_class=forms.SignupForm
    template_name='registration/registration.html'
    success_url=reverse_lazy('login')

class UserUpdateView(UpdateView):
    form_class=forms.UpdateUser
    template_name='registration/update_user.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user