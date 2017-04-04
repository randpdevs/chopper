from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserModel(models.Model):
    Uid=models.AutoField(primary_key=True)
    UserName=models.CharField(max_length=255,blank=False,null=False,unique=True)
    EmailID=models.EmailField(blank=False,null=False)
    Age = models.CharField(max_length=100, blank = True, null = True)
    Country = models.CharField(max_length=255,blank=True, null=True)
    Password=models.CharField(max_length=255, blank=False, null=False)
    UserScore = models.FloatField(default = 0.0, null = True, blank = True)
    def __unicode__(self):
        return unicode(self.UserName)
