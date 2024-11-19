from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    security_question = models.CharField(max_length=255, default="What is your favorite movie?")
    security_answer = models.CharField(max_length=255)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    concentration = models.CharField(max_length=100, blank=True)
    goal1 = models.TextField(blank=True)
    goal2 = models.TextField(blank=True)
    goal3 = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"