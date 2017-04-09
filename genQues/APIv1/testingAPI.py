import requests
import json
from ..models import *

def testSubmitScore(request):
    num = request['num']
    questionID = request['questionID']
    for i in range(0,num):
        rankingObj = rankingSet()
        rankingObj.userName = str(i)
        rankingObj.userScore = i
        rankingObj.correctans = i
        rankingObj.wrongans = 0
        rankingObj.save()
    return '202'






class rankingSet(models.Model):
    resultNumber=models.AutoField(primary_key=True)
    questionID=models.IntegerField(null=False,blank=False)
    userName=models.CharField(max_length=255,null=False,blank=False)
    userScore=models.FloatField(null=False,blank=False)
    correctans = models.IntegerField(null=True, blank = True)
    wrongans=models.IntegerField(null=True,blank=True)