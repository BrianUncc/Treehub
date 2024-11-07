from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

rooms = [
    {'id': 1, 'name': 'Terms and Services.'},
    {'id': 2, 'name': 'Privacy Policy'},
    {'id': 3, 'name': 'Mission Statement'}
]


def home(request):
    return render(request, 'home.html')

def virtualpractice(request):
    return render(request, 'virtualpractice.html')

def progress(request):
    return render(request, 'progress.html')

def messages(request):
    return render(request, 'messages.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')