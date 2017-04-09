import requests
import json
from ..models import *

def testSubmitScore(request):
    num = request['num']
    questionID = request['questionID']
    for i in range(0,num):
        rankingObj = rankingSet()
        rankingObj.questionID = questionID
        rankingObj.userName = str(i)
        rankingObj.userScore = i
        rankingObj.correctans = i
        rankingObj.wrongans = 0
        rankingObj.save()
    return '202'




