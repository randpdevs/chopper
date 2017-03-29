
from ..models import *


from time import time
import json

def getQuestionSet(questionTime):
    questionObj = QuesSet_v1.objects.latest('questionID')
    li = []
    if questionTime <= int(questionObj.questionTimeStamp) + 36000:
        a = json.loads(questionObj.questionSet)
        dataset=[]
        dataset.append({"QuesSet": questionObj.questionID,"EndTime":int(questionObj.questionTimeStamp)+36000,"StartTime":int(time())})

        for item in a:
            dataset.append(item)
        return dataset
    else:
        returnData=[]
        returnData.append({"QuesSet": questionObj.questionID,"EndTime":int(questionObj.questionTimeStamp)+30,"StartTime":int(time())})
        returnData.append({"answer":"Time's up","firstNumber":0,"operator":"~","secondNumber":0})
        return returnData


def getQuestionSetv1(questionTime):
    questionObj = QuesSet_v2.objects.all().order_by('-questionEndStamp')[:10]

    for i in questionObj:
        if questionTime >= i.questionTimeStamp and questionTime <= i.questionEndStamp :
            a = json.loads(i.questionSet)
            dataset = []
            dataset.append({"QuesSet": i.questionID, "EndTime": int(i.questionTimeStamp) + 60,
                            "StartTime": int(time())})
            for item in a:
                dataset.append(item)
            return dataset

        else:
            returnData = []
            returnData.append({"QuesSet": i.questionID, "EndTime": int(i.questionTimeStamp) + 30,
                               "StartTime": int(time())})
            returnData.append({"answer": "Time's up", "firstNumber": 0, "operator": "~", "secondNumber": 0})
            return returnData

import datetime
def getQuestionSetv2():
    today = datetime.datetime.today()
    today_date = str(today).split(' ')[0]
    yy = int(today_date.split('-')[0])
    mm = int(today_date.split('-')[1])
    dd = int(today_date.split('-')[2])
    epochTime_today = int(datetime.datetime(yy, mm, dd, 00, 00).strftime('%s'))

    epochTime = int(today.strftime('%s'))
    try:
        fetchEpochTime=epochTime_today+((epochTime-epochTime_today)/60)*60
        quesObj=QuesSet_v2.objects.filter(questionTimeStamp=fetchEpochTime)
        dataset = []

        for item in quesObj:
            a = json.loads(item.questionSet)
            dataset.append({"QuesSet": item.questionID, "EndTime": int(item.questionEndStamp),
                            "StartTime": int(time()),"BoutEndTime":int(item.questionBoutEndStamp)})

            for item in a:
                dataset.append(item)
        return dataset
    except Exception as e:
        pass
    return ""