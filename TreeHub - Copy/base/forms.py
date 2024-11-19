from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile  
class CustomUserCreationForm(UserCreationForm):
    security_answer = forms.CharField(
        max_length=255,
        required=True,
        label="What is your favorite movie?",
        help_text="Answer to your security question in case you forget your password."
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'security_answer']

class PasswordResetUsernameForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)

class SecurityQuestionForm(forms.Form):
    security_answer = forms.CharField(
        max_length=255,
        required=True,
        label="Answer to your security question"
    )

class SetNewPasswordForm(forms.Form):
    new_password1 = forms.CharField(widget=forms.PasswordInput, label="New password")
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm new password")

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("new_password1")
        password2 = cleaned_data.get("new_password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'concentration', 'goal1', 'goal2', 'goal3']
        labels = {
            'goal1': 'Goal 1',
            'goal2': 'Goal 2',
            'goal3': 'Goal 3',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'concentration': 'Concentration',
        }
