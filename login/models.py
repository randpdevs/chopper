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
    UserScore = models.FloatField(default = 0.00, null = True, blank = False)
    UserFriends = models.ManyToManyField('UserModel',blank=True, null=True)

    class Meta:
        ordering = ["-UserScore"]

    def __unicode__(self):
        return unicode(self.UserName)



class UserStat(models.Model):
    Uid = models.AutoField(primary_key=True)
    UserName = models.ForeignKey('UserModel')
    NumGamePlayed = models.IntegerField(default = 0, blank=True, null= True)
    TotalScore = models.FloatField(default = 0.00, null = True, blank = False)
    TotalCorrectAns = models.IntegerField(default=0, null =True, blank=True)
    TotalWrongAns = models.IntegerField(default=0, null=True, blank = True)

    def __unicode__(self):
        return unicode(self.UserName)


