from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import responses
import json

from APIv1 import genQuestion, getQuestion, getRanking, submitRanking
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
        return Response(returnData, status=status.HTTP_202_ACCEPTED)

class getRankApi(APIView):
    def post(self,request,format=None):
        returnData = getRanking.rankingFunction(request.data)
        return Response(returnData, status=status.HTTP_202_ACCEPTED)


class submitRankApi(APIView):
    def post(self, request, format=None):
        returnData = submitRanking.submitRank(request.data)
        return Response(returnData, status=status.HTTP_202_ACCEPTED)