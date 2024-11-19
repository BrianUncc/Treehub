from django.urls import path
from . import views
<<<<<<< HEAD
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post']
=======
from .views import CustomLogoutView
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> 23b3b29e0b0595e8cfb085a49b69dc21e58669bb

urlpatterns = [
    path('', views.home, name="home"),
    path('homepage/', views.homepage, name="homepage"),
    path('virtualpractice/', views.virtualpractice, name="virtualpractice"),
    path('progress/', views.progress, name="progress"),
<<<<<<< HEAD
    path('messages/', views.messages, name="messages"),
    path('about/', views.about, name="about"),
    path('profile/', views.profile_view, name='profile'),

=======
    path('about/', views.about, name="about"),
    path('messages/', views.custom_messages_view, name='messages'),
    path('profile/', views.profile_view, name='profile'),
    path('view_profile/', views.view_profile, name='view_profile'),  # 确保这个路径存在
>>>>>>> 23b3b29e0b0595e8cfb085a49b69dc21e58669bb

    # Authentication URLs
    path('login/', views.login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('signup/', views.signup, name="signup"),

    # Custom Password Reset with Security Question
<<<<<<< HEAD
    path('password_reset/', views.password_reset_username, name="password_reset"),  # Username entry
    path('password_reset/security_question/', views.password_reset_security_question, name="password_reset_security_question"),  # Security question
    path('password_reset/confirm/', views.password_reset_confirm, name="password_reset_confirm"),  # Password reset confirmation
]
=======
    path('password_reset/', views.password_reset_username, name="password_reset"),
    path('password_reset/security_question/', views.password_reset_security_question, name="password_reset_security_question"),
    path('password_reset/confirm/', views.password_reset_confirm, name="password_reset_confirm"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 23b3b29e0b0595e8cfb085a49b69dc21e58669bb
