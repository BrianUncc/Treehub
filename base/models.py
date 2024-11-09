from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    security_question = models.CharField(max_length=255, default="What is your favorite movie?")
    security_answer = models.CharField(max_length=255)

    concentration = models.CharField(max_length=100, blank=True, null=True)
    goal1 = models.CharField(max_length=255, blank=True, null=True)
    goal2 = models.CharField(max_length=255, blank=True, null=True)
    goal3 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username