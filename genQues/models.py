from __future__ import unicode_literals

from django.db import models

# Create your models here.

class QuesSet_v2(models.Model):
    questionID = models.AutoField(primary_key=True)
    questionDate = models.DateTimeField(null = False, blank = False)
    questionSet = models.TextField(null=False, blank=False)
    questionTimeStamp = models.IntegerField(null=False, blank=False)
    questionEndStamp = models.IntegerField(null=False,blank = False)
    questionBoutEndStamp = models.IntegerField(null = False, blank =False)
    def __unicode__(self):
        return unicode(self.questionID)


#
class rankingSet(models.Model):
    resultNumber=models.AutoField(primary_key=True)
    questionID=models.IntegerField(null=False,blank=False)
    userName=models.CharField(max_length=255,null=False,blank=False)
    userScore=models.FloatField(null=False,blank=False)
    correctans = models.IntegerField(null=False, blank = False)
    wrongans=models.IntegerField(null=False,blank=True)
    def __unicode__(self):
        return unicode(self.resultNumber)


class ApiPassword(models.Model):
    apiID = models.AutoField(primary_key=True)
    apiName = models.TextField(null = False, blank = False)
    apiPassword = models.TextField(null = False, blank = False)
    def __unicode__(self):
        return unicode(self.apiName)


class Top10Model(models.Model):
    rID = models.AutoField(primary_key=True)
    questionID = models.IntegerField(null=False,blank=False)
    top10User = models.TextField(null = False, blank=False)
    def __unicode__(self):
        return unicode(self.questionID)
