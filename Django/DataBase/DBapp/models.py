# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.hashers import make_password

class Prize(models.Model):
    id = models.BigAutoField(primary_key=True)
    prize = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Prize'


class Stories(models.Model):
    id = models.BigAutoField(primary_key=True)
    stories = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField()
    trip = models.ForeignKey('Trip', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Stories'


class Storycomment(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    story = models.ForeignKey(Stories, models.DO_NOTHING, db_column='Story_id')  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    approved = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'StoryComment'


class Trip(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=255)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    date = models.DateField()
    title = models.CharField(max_length=255)
    publish_date = models.DateField(blank=True, null=True)
    votecount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Trip'
    def get_absolute_url(self):
       # What should I do once I create an instance of Trip
       return reverse("trip_detail",kwargs={'pk':self.pk})


class Tripcomment(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    trip = models.ForeignKey(Trip, models.DO_NOTHING, db_column='Trip_id')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    approved = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'TripComment'
    def get_absolute_url(self):
       # What should I do once I create an instance of Trip
       return reverse("trip_detail",kwargs={'pk':self.trip.pk})

    def __str__(self):
        return self.comment
class Userprize(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    prize = models.ForeignKey(Prize, models.DO_NOTHING)
    trip = models.ForeignKey(Trip, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserPrize'


class Votes(models.Model):
    trip = models.ForeignKey(Trip, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Votes'
        unique_together = (('user', 'trip'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
    def get_absolute_url(self):
       # What should I do once I create an instance of Trip
       return reverse("trip_list")
    def make_password(self,raw_password):
       import hashlib
       from random import random
       algo = 'sha1'
       salt = hexdigest(algo, str(random()), str(random()))[:5]
       hash = get_hexdigest(algo, salt, raw_password)
       return '%s$%s$%s' % (algo, salt, hash)


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics',max_length=250, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    profile_id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'user_profile'
    def get_absolute_url(self):
       # What should I do once I create an instance of Trip
       return reverse("get_user_profile",kwargs={'pk':self.user.pk})
