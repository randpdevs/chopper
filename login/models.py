from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserModel(models.Model):
    Uid=models.AutoField(primary_key=True)
    UserName=models.CharField(max_length=255,blank=False,null=False)
    EmailID=models.EmailField(blank=False,null=False)
    Age = models.CharField(max_length=100, blank = False, null = False)
    Country = models.CharField(max_length=255,blank=False, null=False)
    Password=models.CharField(max_length=255, blank=False, null=False)
    def __unicode__(self):
        return unicode(self.UserName)
