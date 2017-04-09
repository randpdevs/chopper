from ..models import  *

def addUserStat(request,userModelObj):

    try:
        statObj = UserStat.objects.get(UserName = userModelObj)
        statObj.NumGamePlayed = statObj.NumGamePlayed + 1
        statObj.TotalScore = statObj.TotalScore + request['userScore']
        statObj.TotalCorrectAns = statObj.TotalCorrectAns + request['correctans']
        statObj.TotalWrongAns = statObj.TotalWrongAns + request['wrongans']
        statObj.save()
        return '202-1'
    except Exception as e:
        statObj = UserStat()
        statObj.UserName = userModelObj
        statObj.NumGamePlayed = statObj.NumGamePlayed + 1
        statObj.TotalScore = statObj.TotalScore + request['userScore']
        statObj.TotalCorrectAns = statObj.TotalCorrectAns + request['correctans']
        statObj.TotalWrongAns = statObj.TotalWrongAns + request['wrongans']
        statObj.save()
        return '202-2'



def gettUserStat(request):
    sendData = []
    try:
        userObj = UserModel.objects.get(UserName = request['UserName'])
    except:
        return '404'
    try:
        statObj = UserStat.objects.get(UserName = userObj)
        sendData.append({"numGamePlayed":statObj.NumGamePlayed, "totalScore":statObj.TotalScore, "totalCorrectAns":statObj.TotalCorrectAns, "totalWrongAns":statObj.TotalWrongAns})
        return sendData
    except:
        return '400'