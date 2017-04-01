from ..models import *

def rankingFunction(data):
    try:
        rankingObj = rankingSet.objects.filter(questionID=data['questionID']).order_by('-userScore')
        sendData = []
        rank = 0
        for i in rankingObj:
            rank = rank+1
            sendData.append({"userName":i.userName,"Rank":rank,"userScore":i.userScore})
        return sendData
    except Exception as e :
        return '400'