from ..models import QuesSet,QuesSet_v1

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