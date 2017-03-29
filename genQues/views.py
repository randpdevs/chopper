from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import responses
import json

from APIv1 import genQuestion, getQuestion, ranking, submitRanking
# Create your views here.
class genQuesAPI(APIView):
	def post(self, request, format=None):
		returnData = genQuestion.quesSet(request.data['firstNumber'], request.data['secondNumber'])
		return Response(returnData, status=status.HTTP_202_ACCEPTED)

class genQuesAPI1(APIView):
	def post(self, request, format=None):
		returnData = genQuestion.quesSet1()
		print type(returnData)
		return Response(returnData, status=status.HTTP_202_ACCEPTED)

class getQuesApi(APIView):
    def post(self, request, format=None):
        returnData = getQuestion.getQuestionSet(request.data['clientTimeStamp'])
        #print type(returnData)
        return Response(returnData, status=status.HTTP_202_ACCEPTED)

class getRankApi(APIView):
    def post(self,request,format=None):
        returnData = ranking.rankingFunction(request.data)
        return Response(returnData, status=status.HTTP_202_ACCEPTED)


class submitRankApi(APIView):
    def post(self, request, format=None):
        returnData = submitRanking.submitRank(request.data)
        return Response(returnData, status=status.HTTP_202_ACCEPTED)

class getQuesApi1(APIView):
    def post(self, request, format=None):
        returnData = getQuestion.getQuestionSetv1(request.data['clientTimeStamp'])
        return Response(returnData, status=status.HTTP_202_ACCEPTED)


class genQuesAPIForTomorrow(APIView):
	def post(self, request, format=None):
		returnData = genQuestion.quesSetForTomorrow()
		return Response(returnData, status=status.HTTP_202_ACCEPTED)
class genQuesAPIForToday(APIView):
	def post(self, request, format=None):
		returnData = genQuestion.quesSetForTomorrow()
		return Response(returnData, status=status.HTTP_202_ACCEPTED)


class getQuesApi2(APIView):
    def post(self, request, format=None):
        returnData = getQuestion.getQuestionSetv2()
        return Response(returnData, status=status.HTTP_202_ACCEPTED)



import datetime
class FetchServerTime(APIView):
    def post(self, request, format=None):
        returnData = str(datetime.datetime.today())
        return Response(returnData, status=status.HTTP_202_ACCEPTED)




