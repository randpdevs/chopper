from ..models import  *
import json

def topTenRanking(request):
    try:
        rankingObj = rankingSet.objects.filter(questionID=request['questionID']).order_by('-userScore')
        objCount = rankingObj.count()
    except Exception as e:
        return '404-1'
    try:
        topTenObj = Top10Model.objects.filter(questionID = request['questionID'])
        if topTenObj.count() == 0:
            topTenObj = Top10Model()
            if objCount < 10:
                rank = 0
                rankData = []
                for i in rankingObj[:objCount]:
                    rank = rank+1
                    rankData.append({"userName":i.userName,"Rank":rank,"userScore":i.userScore})
                topTenObj.questionID = request['questionID']
                topTenObj.top10User = json.dumps(rankData)
                topTenObj.save()
                return '202-1'
            else:
                rank=0
                rankData = []
                for i in rankingObj[:10]:
                    rank = rank+1
                    rankData.append({"userName":i.userName,"Rank":rank,"userScore":i.userScore})
                topTenObj.questionID = request['questionID']
                topTenObj.top10User = json.dumps(rankData)
                topTenObj.save()
            return '202-1'
        else:
            return "202-2"
    except Exception as e:
        return '400-1'