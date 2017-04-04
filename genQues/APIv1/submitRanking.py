from ..models import *
from login.models import UserModel

def submitRank(data):
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
        rankingObj.correctans = data['correctans']
        rankingObj.wrongans = data['wrongans']
        rankingObj.save()
        return "202-1"
    except Exception as e:
        return '400'
