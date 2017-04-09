from ..models import *
#
def rankingFunction(data):
    try:
        rankingObj = rankingSet.objects.filter(questionID=data['questionID'])
        sendData = []
        rank = 0
        for i in rankingObj:
            rank = rank+1
            sendData.append({"userName":i.userName,"Rank":rank,"userScore":i.userScore,"correctans":i.correctans,"wrongans":i.wrongans})
        return sendData
    except Exception as e :
        return '400'




def rankingFunctionv_1(data):
    try:
        rankingObj = rankingSet.objects.filter(questionID=data['questionID']).order_by('-userScore')
        countObj = rankingObj.count()
        rankData = []
        userRank = 0
        if countObj < 10:
            rank = 0
            for i in rankingObj[:countObj]:
                rank = rank + 1
                if i.userName == str(data['userName']):
                    userRank = rank-1
                rankData.append({"userName": i.userName, "Rank": rank, "userScore": i.userScore})
            print userRank
        else:
            rank = 0
            for i in rankingObj:
                rank = rank + 1
                if rank <=10:
                    rankData.append({"userName": i.userName, "Rank": rank, "userScore": i.userScore})
                if i.userName == str(data['userName']):
                    userRank = rank-1



            print userRank
        if userRank >= 10:
            try:
                rankData.append({"userName": rankingObj[userRank-2].userName, "Rank": userRank-1,
                                 "userScore": rankingObj[ userRank].userScore})
                rankData.append({"userName": rankingObj[userRank - 1].userName, "Rank": userRank,
                              "userScore": rankingObj[userRank].userScore})
            except Exception as e:
                print e
                pass
            rankData.append({"userName": rankingObj[userRank].userName, "Rank": userRank+1,
                                 "userScore": rankingObj[ userRank].userScore})
            try:
                rankData.append({"userName": rankingObj[userRank+1].userName, "Rank": userRank+2,
                                 "userScore": rankingObj[ userRank].userScore})
                rankData.append({"userName": rankingObj[userRank+2].userName, "Rank": userRank+3,
                              "userScore": rankingObj[userRank].userScore})
            except Exception as e:
                print e
                pass

            return rankData
        else:
            return rankData
        return rankData
    except Exception as e :
        return '400'



        # for i in rankingObj[userRank-3:userRank]:
        #     try:
        #         rankData.append({"userName": i.userName, "Rank": rank, "userScore": i.userScore})
        #     except Exception as e:
        #         print e
        # for i in rankingObj[userRank+1:userRank+3]:
        #     try:
        #         rankData.append({"userName": i.userName, "Rank": rank, "userScore": i.userScore})
        #     except Exception as e :
        #         print e