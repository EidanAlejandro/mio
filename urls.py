from django.urls import path
from .views import SignUpView, ProfileUpdate, EmailUpdate
from django.contrib import admin
from registration import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),  
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),       
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    ]
