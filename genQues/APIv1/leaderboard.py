from login.models import UserModel

def getLeaderboard():
    try:
        leaderboardObj = UserModel.objects.all().order_by('-UserScore')[:10]
        sendData = []
        rank = 0
        for i in leaderboardObj:
            rank = rank+1
            sendData.append({"Rank":rank,"userName":i.UserName,"Score":i.UserScore})
        return sendData
    except:
        return '400'
