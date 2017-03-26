from ..models import *

def submitRank(data):
    rankingObj = rankingSet()
    rankingObj.questionA = data['questionID']
    rankingObj.userName = data['userName']
    rankingObj.userScore = data['userScore']
    rankingObj.save()
    return "Success"