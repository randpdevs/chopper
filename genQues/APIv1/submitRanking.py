from ..models import *
from login.models import UserModel,UserStat
from time import time
from login.APIv1 import userStatAPI

def submitRank(data):
    currentEpoch = int(time())
    try:
        quesObj = QuesSet_v2.objects.get(questionID = data['questionID'])
    except:
        return '404'
    print currentEpoch, quesObj.questionBoutEndStamp, quesObj.questionTimeStamp
    if currentEpoch <= int(quesObj.questionBoutEndStamp) and currentEpoch >= int(quesObj.questionTimeStamp):
        try:
            rankingObj = rankingSet()
            rankingObj.questionID = data['questionID']
            rankingObj.userName = data['userName']
            rankingObj.userScore = data['userScore']
            try:
                userModelObj = UserModel.objects.get(UserName = data['userName'])
                userModelObj.UserScore = max(data['userScore'],userModelObj.UserScore)
                userModelObj.save()
            except :
                pass
            try:
                userStatAPI.addUserStat(data,userModelObj)
            except Exception as e:
                pass

            rankingObj.correctans = data['correctans']
            rankingObj.wrongans = data['wrongans']
            rankingObj.save()
            return "202-2"
        except Exception as e:
            return '400'
    else:
        return '202-1'
