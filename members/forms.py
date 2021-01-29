from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from blog.models import Profile

class SignupForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    second_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','second_name','email','password1','password2')
        
    def __init__(self, *args, **kwargs):

            super(SignupForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['class']='form-control'
            self.fields['password1'].widget.attrs['class']='form-control'
            self.fields['password2'].widget.attrs['class']='form-control'

class UpdateUser(UserChangeForm):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class':'form-control'}))
    is_superuser=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    last_login=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','is_superuser','is_staff','is_active','last_login')

class PasswordUpdationForm(PasswordChangeForm):
    old_password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    class Meta:
        model=User
        fields=('old_password','new_password1','new_password2')

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile

        fields=('bio','profile_pic','linkedin_url','codechef_url','codeforces_url')
        widgets={
            'bio':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Bio'}),
           
            'linkedin_url':forms.TextInput(attrs={'class':'form-control'}),
            'codechef_url':forms.TextInput(attrs={'class':'form-control'}),
            'codeforces_url':forms.TextInput(attrs={'class':'form-control'}),
        }