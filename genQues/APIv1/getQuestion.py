from ..models import QuesSet,QuesSet_v1
import datetime
import json

def getQuestionSet(questionTime):
    questionObj = QuesSet_v1.objects.latest('questionID')
    li = []
    if questionTime <= int(questionObj.questionTimeStamp) + 3600:
        a = json.loads(questionObj.questionSet)
        dataset=[]
        dataset.append({"QuesSet": questionObj.questionID})

        for item in a:
            dataset.append(item)
        return dataset
    else:
        return "Time's up sucker"



