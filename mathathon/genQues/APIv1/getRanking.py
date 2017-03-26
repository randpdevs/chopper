from ..models import *

def rankingFunction(data):
    rankingObj = rankingSet.objects.filter(questionA=data['questionID']).order_by('-userScore')
    print rankingObj
    sendData = []
    rank = 0
    for i in rankingObj:
        rank = rank+1
        sendData.append({"userName":i.userName,"Rank":rank})
    return sendData




