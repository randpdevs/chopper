from ..models import *

def submitRank(data):
    try:
        rankingObj = rankingSet()
        rankingObj.questionA = data['questionID']
        rankingObj.userName = data['userName']
        rankingObj.userScore = data['userScore']
        rankingObj.save()
        return "Success"
    except Exception as e:
        print e
        return '400'