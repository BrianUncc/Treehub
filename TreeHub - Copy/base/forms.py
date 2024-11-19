from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from .models import UserProfile  
=======
from .models import UserProfile

>>>>>>> 23b3b29e0b0595e8cfb085a49b69dc21e58669bb
class CustomUserCreationForm(UserCreationForm):
    security_answer = forms.CharField(
        max_length=255,
        required=True,
<<<<<<< HEAD
        label="What is your favorite movie?",
        help_text="Answer to your security question in case you forget your password."
    )

=======
        label="What is your favorite movie?",  # Set the label to the question
        help_text="Answer to your security question in case you forget your password."
    )
    
>>>>>>> 23b3b29e0b0595e8cfb085a49b69dc21e58669bb
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'security_answer']

class PasswordResetUsernameForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)

class SecurityQuestionForm(forms.Form):
<<<<<<< HEAD
    security_answer = forms.CharField(
        max_length=255,
        required=True,
        label="Answer to your security question"
    )
=======
    security_answer = forms.CharField(max_length=255, required=True, label="Answer to your security question")
>>>>>>> 23b3b29e0b0595e8cfb085a49b69dc21e58669bb

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

<<<<<<< HEAD
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
=======
# This is the form operates with the user's profile information
class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ['concentration', 'goal1', 'goal2', 'goal3', 'avatar', 'introduction']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        user_profile = super(UserProfileForm, self).save(commit=False)
        user_profile.user.email = self.cleaned_data['email']
        if commit:
            user_profile.user.save()
            user_profile.save()
        return user_profile

>>>>>>> 23b3b29e0b0595e8cfb085a49b69dc21e58669bb
