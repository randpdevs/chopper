import random
import time, threading
import json
from time import time
from datetime import datetime
from ..models import QuesSet, QuesSet_v1

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
    quesList = []
    for i in range(0,10):
        startOfRange=1
        endOfRange=10
        quesList.append(random.choice([addition(startOfRange, endOfRange),
        multiplication(startOfRange, endOfRange), division(startOfRange, endOfRange),
        subtraction(startOfRange, endOfRange)]))
    questionObj = QuesSet_v1()
    questionObj.questionSet=json.dumps(quesList)
    questionObj.questionTimeStamp=int(time())
    questionObj.save()
    return quesList

