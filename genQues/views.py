from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import responses
import json
import datetime
from APIv1 import genQuestion, getQuestion, getRanking, submitRanking, apiPassword
# Create your views here.
class getRankApi(APIView):


    def post(self,request,format=None):


        returnData = getRanking.rankingFunction(request.data)
        if returnData != '400':
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        else :
            return Response(returnData, status = status.HTTP_400_BAD_REQUEST)



class submitRankApi(APIView):


    def post(self, request, format=None):


        returnData = submitRanking.submitRank(request.data)
        return Response(returnData, status=status.HTTP_202_ACCEPTED)


class genQuesAPIForTomorrow(APIView):


	def post(self, request, format=None):


		returnData = genQuestion.quesSetForTomorrow(request.data)
		return Response(returnData, status=status.HTTP_202_ACCEPTED)


class genQuesAPIForToday(APIView):


	def post(self, request, format=None):


		returnData = genQuestion.quesSetForToday(request.data)
		return Response(returnData, status=status.HTTP_202_ACCEPTED)


class getQuesApi2(APIView):


    def post(self, request, format=None):


        returnData = getQuestion.getQuestionSetv2(request.data)
        return Response(returnData, status=status.HTTP_202_ACCEPTED)


class DeleteQues(APIView):


    def post(self, request, format=None):
        returnData = genQuestion.deleteQuestion(request.data)
        return Response(returnData, status=status.HTTP_202_ACCEPTED)


class FetchServerTime(APIView):


    def post(self, request, format=None):


        returnData = str(datetime.datetime.today())
        return Response(returnData, status=status.HTTP_202_ACCEPTED)


class SetApiPassword(APIView):


    def post(self, request, format=None):


        returnData = apiPassword.setPassword(request.data)
        if returnData != '400':
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(returnData, status = status.HTTP_400_BAD_REQUEST)


class ModifyApiPassword(APIView):


    def post(self, request, format=None):


        returnData = apiPassword.modifyPassword(request.data)
        if returnData != '400':
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(returnData, status = status.HTTP_400_BAD_REQUEST)





