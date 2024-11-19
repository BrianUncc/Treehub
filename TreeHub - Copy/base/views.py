from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .models import UserProfile
from .forms import (
    PasswordResetUsernameForm, SecurityQuestionForm, 
    SetNewPasswordForm, CustomUserCreationForm, UserProfileForm
)
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

<<<<<<< HEAD
# Static room definitions
=======
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserProfileForm
from django.contrib.auth.views import LogoutView



>>>>>>> 23b3b29e0b0595e8cfb085a49b69dc21e58669bb
rooms = [
    {'id': 1, 'name': 'Terms and Services.'},
    {'id': 2, 'name': 'Privacy Policy'},
    {'id': 3, 'name': 'Mission Statement'}
]

<<<<<<< HEAD
# View Definitions
=======

>>>>>>> 23b3b29e0b0595e8cfb085a49b69dc21e58669bb
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def virtualpractice(request):
    return render(request, 'virtualpractice.html')

def progress(request):
    return render(request, 'progress.html')

<<<<<<< HEAD
def messages(request):
=======
def custom_messages_view(request):
>>>>>>> 23b3b29e0b0595e8cfb085a49b69dc21e58669bb
    return render(request, 'messages.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.userprofile.security_answer = form.cleaned_data.get('security_answer')
            user.userprofile.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def password_reset_username(request):
    if request.method == 'POST':
        form = PasswordResetUsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = get_object_or_404(User, username=username)
            request.session['reset_user_id'] = user.id
            return redirect('password_reset_security_question')
    else:
        form = PasswordResetUsernameForm()
    return render(request, 'password_reset_username.html', {'form': form})

def password_reset_security_question(request):
    user_id = request.session.get('reset_user_id')
    if not user_id:
        return redirect('password_reset_username')
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = SecurityQuestionForm(request.POST)
        if form.is_valid():
            security_answer = form.cleaned_data.get('security_answer')
            if security_answer.lower() == user.userprofile.security_answer.lower():
                return redirect('password_reset_confirm')
            else:
                messages.error(request, 'Incorrect answer to the security question.')
    else:
        form = SecurityQuestionForm()
    return render(request, 'password_reset_security_question.html', {'form': form, 'security_question': user.userprofile.security_question})

def password_reset_confirm(request):
    user_id = request.session.get('reset_user_id')
    if not user_id:
        return redirect('password_reset_username')
    
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = SetNewPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password1')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
<<<<<<< HEAD
            messages.success(request, 'Your password has been reset successfully.')
            return redirect('login')  # Redirect to the login page after reset
    else:
        form = SetNewPasswordForm()
        
    return render(request, 'password_reset_confirm.html', {'form': form})

@login_required
def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')  # Adjust this to your account/profile URL name
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'profile.html', {'form': form})
=======
            
            
            return render(request, 'password_reset_confirm.html', {'password_reset_success': True})
    else:
        form = SetNewPasswordForm()
        
    return render(request, 'password_reset_confirm.html', {'form': form, 'password_reset_success': False})


# Below Operates with account/profile
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    
    return render(request, 'profile.html', {'form': form})

@login_required
def view_profile(request):
    return render(request, 'view_profile.html', {'userprofile': request.user.userprofile})

class CustomLogoutView(LogoutView):
    next_page = 'home'
>>>>>>> 23b3b29e0b0595e8cfb085a49b69dc21e58669bb
