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
        rankingObj = rankingSet.objects.filter(questionID=data['questionID'])
        countObj = rankingObj.count()
        rankData = []
        userRank = 0
        rankData.append({"TotalRank":countObj})
        if countObj < 10:
            rank = 0
            for i in rankingObj[:countObj]:
                rank = rank + 1
                if i.userName == str(data['userName']):
                    userRank = rank-1
                rankData.append({"userName": i.userName, "Rank": rank, "userScore": i.userScore,
                                 "correctans":i.correctans,"wrongans":i.wrongans})

        else:
            rank = 0
            for i in rankingObj:
                rank = rank + 1
                if rank <=10:
                    rankData.append({"userName": i.userName, "Rank": rank, "userScore": i.userScore,
                                     "correctans":i.correctans,"wrongans":i.wrongans})
                if i.userName == str(data['userName']):
                    userRank = rank-1

        rankData.append({"userName": "*", "Rank": "*",
                         "userScore": "*",
                         "correctans": "*",
                         "wrongans": "*"})

        if userRank >= 10:
            try:
                rankData.append({"userName": rankingObj[userRank-2].userName, "Rank": userRank-1,
                                 "userScore": rankingObj[ userRank-2].userScore,"correctans":rankingObj[userRank-2].correctans,
                                 "wrongans":rankingObj[userRank-2].wrongans})
                rankData.append({"userName": rankingObj[userRank - 1].userName, "Rank": userRank,
                              "userScore": rankingObj[userRank].userScore,"correctans":rankingObj[userRank-1].correctans,
                                 "wrongans":rankingObj[userRank-1].wrongans})
            except Exception as e:
               pass
            rankData.append({"userName": rankingObj[userRank].userName, "Rank": userRank+1,
                                 "userScore": rankingObj[ userRank].userScore,"correctans":rankingObj[userRank].correctans
                                ,"wrongans":rankingObj[userRank].wrongans})
            try:
                rankData.append({"userName": rankingObj[userRank+1].userName, "Rank": userRank+2,
                                 "userScore": rankingObj[ userRank].userScore,"correctans":rankingObj[userRank+1].correctans,
                                 "wrongans":rankingObj[userRank+1].wrongans})
                rankData.append({"userName": rankingObj[userRank+2].userName, "Rank": userRank+3,
                              "userScore": rankingObj[userRank].userScore,"correctans":rankingObj[userRank+2].correctans,
                                 "wrongans":rankingObj[userRank+2].wrongans})
            except Exception as e:
                pass
            rankData.append({"userName": "*", "Rank": "*",
                             "userScore": "*",
                             "correctans": "*",
                             "wrongans": "*"})

            return rankData
        else:
            return rankData
        return rankData
    except Exception as e :
        return '400'


