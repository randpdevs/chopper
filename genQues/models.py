from __future__ import unicode_literals

from django.db import models

# Create your models here.

class QuesSet(models.Model):
    questionID=models.AutoField(primary_key=True)
    questionSet=models.TextField(null=False,blank=False)
    questionTimeStamp=models.DateTimeField(null=False,blank=False)
    def __unicode__(self):
        return unicode(self.questionID)


class QuesSet_v1(models.Model):
    questionID=models.AutoField(primary_key=True)
    questionSet=models.TextField(null=False,blank=False)
    questionTimeStamp=models.IntegerField(null=False,blank=False)
    def __unicode__(self):
        return unicode(self.questionID)

class QuesSet_v2(models.Model):
    questionID = models.AutoField(primary_key=True)
    questionDate = models.CharField(max_length=255,null = False, blank = False)
    questionSet = models.TextField(null=False, blank=False)
    questionTimeStamp = models.IntegerField(null=False, blank=False)
    questionEndStamp = models.IntegerField(null=False,blank = False)
    questionBoutEndStamp = models.IntegerField(null = False, blank =False)
    def __unicode__(self):
        return unicode(self.questionID)


#
class rankingSet(models.Model):
    resultNumber=models.AutoField(primary_key=True)
    questionA=models.IntegerField(null=False,blank=False)
    userName=models.CharField(max_length=255,null=False,blank=False)
    userScore=models.FloatField(null=False,blank=False)
    def __unicode__(self):
        return unicode(self.resultNumber)
