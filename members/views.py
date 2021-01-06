from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,UpdateView,DetailView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import views
from django.urls import reverse_lazy
from members import forms
from blog.models import Profile
# Create your views here.

class ProfileView(DetailView):
    model=Profile
    template_name='registration/profile_page.html'

    def get_context_data(self,*args,**kwargs):
        users=Profile.objects.all()
        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])
        new_context=super(ProfileView,self).get_context_data(*args,**kwargs)
        new_context['page_user']=page_user
        return new_context

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

class EditProfilePageView(UpdateView):
    model=Profile
    template_name='registration/edit_profile_page.html'
    fields=['bio','profile_pic','linkedin_url','codechef_url','codeforces_url']
    success_url=reverse_lazy('home')

class CreateProfileView(CreateView):
    model=Profile
    form_class=forms.CreateProfileForm
    template_name="registration/create_profile.html"
    # fields='__all__'
    # success_url=reverse_lazy('home')
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
