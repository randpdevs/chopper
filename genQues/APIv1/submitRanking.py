from ..models import *

def submitRank(data):
    try:
        rankingObj = rankingSet()
        rankingObj.questionID = data['questionID']
        rankingObj.userName = data['userName']
        rankingObj.userScore = data['userScore']
        rankingObj.save()
        return "202-1"
    except Exception as e:
        print e
        return '400'
