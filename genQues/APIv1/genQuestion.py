import random
import bcrypt
import time, threading
import json
from time import time
import datetime
from ..models import *
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
    resultJson = {'firstNumber' : firstNumber, 'secondNumber' : secondNumber, 'operator': 'x', 'answer' : result}
    return resultJson


def subtraction(startOfRange, endOfRange):


    firstNumber = random.randint(startOfRange, endOfRange)
    secondNumber = random.randint(startOfRange, firstNumber)
    result = firstNumber - secondNumber
    resultJson = {'firstNumber' : firstNumber, 'secondNumber' : secondNumber, 'operator': '-', 'answer' : result}
    return resultJson


def quesSetForTomorrow(request):
    try:
        apiPass = ApiPassword.objects.get(apiName='quesSetForTomorrow').apiPassword
    except:
        return '404-1'
    if bcrypt.checkpw(str(request['password']),str(apiPass)):
        try:
            today = datetime.datetime.now().date()
            tomorrow = today + datetime.timedelta(days=1)
            epochTime = int(tomorrow.strftime('%s'))
            flag=False
            try:
                quesObjCount=QuesSet_v2.objects.filter(questionDate=tomorrow).count()
                if quesObjCount==0:
                    flag=True
            except Exception as e:
                return '404'
            if flag:
                for i in range(1,1441):
                    questionSetObj = QuesSet_v2()
                    questionSetObj.questionDate = tomorrow
                    quesList = []
                    for j in range(0,120):
                        quesList.append(random.choice([addition(1, 100),
                        multiplication(1, 15), division(1, 100),
                        subtraction(1, 100)]))
                    questionSetObj.questionSet = json.dumps(quesList)
                    questionSetObj.questionTimeStamp = epochTime
                    epochTime = epochTime+30
                    questionSetObj.questionEndStamp = epochTime
                    epochTime = epochTime+30
                    questionSetObj.questionBoutEndStamp = epochTime
                    questionSetObj.save()
                return "202-1"
            else:
                return "202-2"
        except Exception as e:
            return '400'
    else:
        return '409-1'


def quesSetForToday(request):
    try:
        apiPass = ApiPassword.objects.get(apiName= 'quesSetForToday').apiPassword
    except Exception as e:
        print e
        return '404-1'
    if bcrypt.checkpw(str(request['password']), str(apiPass)):
        today = datetime.datetime.now().date()
        epochTime = int(today.strftime('%s'))
        flag=False
        try:
            quesObjCount=QuesSet_v2.objects.filter(questionDate=today).count()
            if quesObjCount==0:
                flag=True
        except Exception as e:
            return "400"
        if flag:

            for i in range(1,1441):
                questionSetObj = QuesSet_v2()
                questionSetObj.questionDate = today
                quesList = []
                for j in range(0,120):
                    startOfRange=1
                    endOfRange=10
                    quesList.append(random.choice([addition(1, 100),
                    multiplication(1, 15), division(1, 100),
                    subtraction(1, 100)]))
                questionSetObj.questionSet = json.dumps(quesList)
                questionSetObj.questionTimeStamp = epochTime
                epochTime = epochTime+30
                questionSetObj.questionEndStamp = epochTime
                epochTime = epochTime+30
                questionSetObj.questionBoutEndStamp = epochTime
                questionSetObj.save()
            return "202-1"
        else:
            return "202-2"
    else:
        return "409-1"


def deleteQuestion(request):
    try:
        apiPass = ApiPassword.objects.get(apiName = 'deleteQuestion').apiPassword
    except Exception as e :
        return '404-1'
    if bcrypt.checkpw(str(request['password']), str(apiPass)):
        try:
            if request['day'] == 'tomorrow':
                quesObj = QuesSet_v2.objects.filter(questionDate=(datetime.datetime.now().date()+datetime.timedelta(days=1)))
            elif request['day'] == 'yesterday':
                quesObj = QuesSet_v2.objects.filter(questionDate=(datetime.datetime.now().date()-datetime.timedelta(days=1)))
            elif request['day'] == 'today':
                quesObj = QuesSet_v2.objects.filter(questionDate=datetime.datetime.now().date())
            quesObj.delete()
            return "202-1"

        except Exception as e:
            print e
            return "400-1"
    else:
        return "409-1"
