from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class AuthUser(AbstractBaseUser):
    #password = models.CharField(max_length=128)
    #last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField(default = 0)
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.IntegerField(default=0)
    is_active = models.IntegerField(default=1)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    class Meta:
        managed = False
        db_table = 'auth_user'
class AuthUserprofile(models.Model):
    name = models.CharField(max_length=255)
    meta = models.TextField()
    courseware = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    year_of_birth = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    level_of_education = models.CharField(max_length=6, blank=True, null=True)
    mailing_address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    goals = models.TextField(blank=True, null=True)
    allow_certificate = models.IntegerField()
    bio = models.CharField(max_length=3000, blank=True, null=True)
    profile_image_uploaded_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, unique=True)

    class Meta:
        managed = False
        db_table = 'auth_userprofile'

    @classmethod
    def create(cls, fullname,user , city):
        profile = cls(name = fullname , city = city , user_id= user.id,
                   courseware= 'course.xml', meta = '{"session_id": null}' , allow_certificate = 1 , country= 'IN')
        # do something with the book
        return profile