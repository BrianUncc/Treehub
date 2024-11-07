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
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('signup/', views.signup, name="signup"),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
