from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


class ReviewUser(models.Model):
    first_Q = models.TextField()
    second_Q = models.TextField()
    third_Q = models.TextField()
    forth_Q = models.TextField()
    name = models.ForeignKey('username.User')
    date = models.DateTimeField(blank=True,null=True)

    def submit(self):
        self.date = timezone.now()
        self.save()


    def __str__(self):
        return self.name
