from ..models import *

def rankingFunction(data):
    rankingObj = rankingSet.objects.filter(questionA=data['questionID']).order_by('-userScore')
    sendData = []
    rank = 0
    for i in rankingObj:
        rank = rank+1
        sendData.append({"userName":i.userName,"Rank":rank,"userScore":i.userScore})
    return sendData