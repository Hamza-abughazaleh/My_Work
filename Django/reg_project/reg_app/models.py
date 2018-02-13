from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class UserPorfileInfo(models.Model):
    user = models.OneToOneField(User)


    #additional
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    creat_date = models.DateTimeField(default=timezone.now())
    piblished_date = models.DateTimeField(blank=True,null=True)


    def __str__(self):
        return self.title
