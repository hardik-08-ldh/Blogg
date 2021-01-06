from django.urls import path
from members import views
from django.contrib.auth import views as auth_views
# this is required for password change /|\
urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='register'),
    path('edit_user/',views.UserUpdateView.as_view(),name='update_user'),
    # path('password/',auth_views.PasswordChangeView.as_view())
    # this is the by default url for password change /|\ this will open the default django password change page.
    # path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html')),
    # this will not work if we want to have success url for us/|\
    path('password/',views.UpdatePasswordView.as_view(template_name='registration/password_change.html')),
    path('<int:pk>/profile/',views.ProfileView.as_view(),name='profile'),
    path('<int:pk>/edit_profile_page/',views.EditProfilePageView.as_view(),name='edit_profile'),
    path('create_profile/',views.CreateProfileView.as_view(),name='create_profile'),
]