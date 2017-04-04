from ..models import *
import datetime
from time import time
import json
from . import deleteRanking
import bcrypt

def getQuestionSetv2(request):

    try:
        apiPass = ApiPassword.objects.get(apiName='getQuestion').apiPassword
    except:
        return "404-1"
    if bcrypt.checkpw(str(request['password']), str(apiPass)):
        today = datetime.datetime.today()
        epochTime_today = int(datetime.datetime.now().date().strftime('%s'))
        epochTime = int(today.strftime('%s'))
        endTime=""
        try:
            fetchEpochTime=epochTime_today+((epochTime-epochTime_today)/60)*60
            quesObj=QuesSet_v2.objects.filter(questionTimeStamp=fetchEpochTime)
            dataset = []
            for item in quesObj:
                a = json.loads(item.questionSet)
                dataset.append({"QuesSet": item.questionID, "EndTime": int(item.questionEndStamp),
                                "StartTime": int(time()),"BoutEndTime":int(item.questionBoutEndStamp)})
                endTime=int(item.questionBoutEndStamp)
                for item in a:
                    dataset.append(item)
            if (endTime-epochTime>0):
                deleteRanking.deletePreviousRank(request['password'])
            return dataset
        except Exception as e:
            return str(e)
    else:
        return "409-1"

