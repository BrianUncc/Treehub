from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post']

urlpatterns = [
    path('', views.home, name="home"),
    path('homepage/', views.homepage, name="homepage"),
    path('virtualpractice/', views.virtualpractice, name="virtualpractice"),
    path('progress/', views.progress, name="progress"),
    path('messages/', views.messages, name="messages"),

    # Authentication URLs
    path('login/', views.login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('signup/', views.signup, name="signup"),

    # Custom Password Reset with Security Question
    path('password_reset/', views.password_reset_username, name="password_reset"),  # Username entry
    path('password_reset/security_question/', views.password_reset_security_question, name="password_reset_security_question"),  # Security question
    path('password_reset/confirm/', views.password_reset_confirm, name="password_reset_confirm"),  # Password reset confirmation
]
