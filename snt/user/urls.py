from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
app_name = 'user'
urlpatterns = [
    path('', views.SignUp.as_view(), name='all'),
    path('userprofile/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('passwordchange/', views.PasswordChangeView.as_view(), name='password_change'),
]
