<<<<<<< HEAD
from django.contrib.auth.models import User
from django.db import models
=======
from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
>>>>>>> 23b3b29e0b0595e8cfb085a49b69dc21e58669bb

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    security_question = models.CharField(max_length=255, default="What is your favorite movie?")
    security_answer = models.CharField(max_length=255)
<<<<<<< HEAD

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
=======
    concentration = models.CharField(max_length=100, blank=True, null=True)
    goal1 = models.CharField(max_length=255, blank=True, null=True)
    goal2 = models.CharField(max_length=255, blank=True, null=True)
    goal3 = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)  # 新增字段

    def __str__(self):
        return self.user.username

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return static('base/default-avatar.png')
>>>>>>> 23b3b29e0b0595e8cfb085a49b69dc21e58669bb
