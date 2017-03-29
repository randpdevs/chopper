import random
import time, threading
import json
from time import time
from datetime import datetime
from ..models import QuesSet, QuesSet_v1,QuesSet_v2
import datetime

def factors(n):    
    return set(reduce(list.__add__, 
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def division(startOfRange, endOfRange):
    firstNumber = random.randint(startOfRange, endOfRange)
    factorsFirstNumber = factors(firstNumber)
    secondNumber = random.choice(random.sample(factorsFirstNumber,1))
    result = firstNumber/secondNumber
    resultJson = {'firstNumber' : firstNumber, 'secondNumber' : secondNumber, 'operator': '/','answer' : result}
    return resultJson

def addition(startOfRange, endOfRange):
    firstNumber = random.randint(startOfRange, endOfRange)
    secondNumber = random.randint(startOfRange, endOfRange)
    result = firstNumber + secondNumber
    resultJson = {'firstNumber' : firstNumber, 'secondNumber' : secondNumber, 'operator': '+', 'answer' : result}
    return resultJson

def multiplication(startOfRange, endOfRange):
    firstNumber = random.randint(startOfRange, endOfRange)
    secondNumber = random.randint(startOfRange, endOfRange)
    result = firstNumber * secondNumber
    resultJson = {'firstNumber' : firstNumber, 'secondNumber' : secondNumber, 'operator': '*', 'answer' : result}
    return resultJson

def subtraction(startOfRange, endOfRange):
    firstNumber = random.randint(startOfRange, endOfRange)
    secondNumber = random.randint(startOfRange, firstNumber)
    result = firstNumber - secondNumber
    resultJson = {'firstNumber' : firstNumber, 'secondNumber' : secondNumber, 'operator': '-', 'answer' : result}
    return resultJson

def quesSet(startOfRange, endOfRange):
    quesList = [] 
    for i in range(0,120):
        quesList.append(random.choice([addition(startOfRange, endOfRange),
         multiplication(startOfRange, endOfRange), division(startOfRange, endOfRange),
          subtraction(startOfRange, endOfRange)]))
    questionObj = QuesSet()
    questionObj.questionSet=quesList
    questionObj.questionTimeStamp=datetime.now()
    questionObj.save()
    return quesList

def quesSet1():
    for i in range(0,10):
        quesList = []
        for j in range(0,10):
            startOfRange=1
            endOfRange=10
            quesList.append(random.choice([addition(startOfRange, endOfRange),
            multiplication(startOfRange, endOfRange), division(startOfRange, endOfRange),
            subtraction(startOfRange, endOfRange)]))
        questionObj = QuesSet_v1()
        questionObj.questionSet=json.dumps(quesList)
        questionObj.questionTimeStamp=int(time())

        questionObj.save()
    return "generated"

def quesSetForTomorrow():
    today = datetime.datetime.today()
    tomorrow = today + datetime.timedelta(days=1)
    tomorrow = str(tomorrow).split(' ')[0]
    yy=int(tomorrow.split('-')[0])
    mm=int(tomorrow.split('-')[1])
    dd=int(tomorrow.split('-')[2])
    epochTime = int(datetime.datetime(yy,mm,dd,00,00).strftime('%s'))


    flag=False
    try:
        quesObjCount=QuesSet_v2.objects.filter(questionDate=tomorrow).count()
        if quesObjCount==0:
            flag=True
    except Exception as e:
        pass
    if flag:
        #1441
        for i in range(1,1441):
            questionSetObj = QuesSet_v2()
            questionSetObj.questionDate = tomorrow
            quesList = []
            for j in range(0,10):
                startOfRange=1
                endOfRange=10
                quesList.append(random.choice([addition(startOfRange, endOfRange),
                multiplication(startOfRange, endOfRange), division(startOfRange, endOfRange),
                subtraction(startOfRange, endOfRange)]))
            questionSetObj.questionSet = json.dumps(quesList)
            questionSetObj.questionTimeStamp = epochTime
            epochTime = epochTime+30
            questionSetObj.questionEndStamp = epochTime
            epochTime = epochTime+30
            questionSetObj.questionBoutEndStamp = epochTime
            questionSetObj.save()
        return "generated"
    else:
        return "Already_generated"


def quesSetForToday():
    today = datetime.datetime.today()
    tomorrow = str(today).split(' ')[0]
    yy=int(tomorrow.split('-')[0])
    mm=int(tomorrow.split('-')[1])
    dd=int(tomorrow.split('-')[2])
    epochTime = int(datetime.datetime(yy,mm,dd,00,00).strftime('%s'))
    flag=False
    try:
        quesObjCount=QuesSet_v2.objects.filter(questionDate=tomorrow).count()
        if quesObjCount==0:
            flag=True
    except Exception as e:
        pass
    if flag:
        #1441
        for i in range(1,1441):
            questionSetObj = QuesSet_v2()
            questionSetObj.questionDate = tomorrow
            quesList = []
            for j in range(0,10):
                startOfRange=1
                endOfRange=10
                quesList.append(random.choice([addition(startOfRange, endOfRange),
                multiplication(startOfRange, endOfRange), division(startOfRange, endOfRange),
                subtraction(startOfRange, endOfRange)]))
            questionSetObj.questionSet = json.dumps(quesList)
            questionSetObj.questionTimeStamp = epochTime
            epochTime = epochTime+30
            questionSetObj.questionEndStamp = epochTime
            epochTime = epochTime+30
            questionSetObj.questionBoutEndStamp = epochTime
            questionSetObj.save()
        return "generated"
    else:
        return "Already_generated"

