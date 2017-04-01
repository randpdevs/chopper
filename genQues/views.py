from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import responses
import json
import datetime
from APIv1 import genQuestion, getQuestion, getRanking, submitRanking, apiPassword, deleteRanking
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
        if returnData == '404-1':
            return Response(returnData, status=status.HTTP_404_NOT_FOUND)
        elif returnData == '202-1':
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        elif returnData == '202-2':
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        elif returnData == '400':
            return Response(returnData, status=status.HTTP_404_NOT_FOUND)
        elif returnData == '409-1':
            return Response(returnData, status=status.HTTP_409_CONFLICT)


class genQuesAPIForToday(APIView):
    def post(self, request, format=None):
        returnData = genQuestion.quesSetForToday(request.data)
        if returnData == '404-1':
            return Response(returnData, status=status.HTTP_404_NOT_FOUND)
        elif returnData == '202-1':
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        elif returnData == '202-2':
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        elif returnData == '400':
            return Response(returnData, status=status.HTTP_400_BAD_REQUEST)
        elif returnData == '409-1':
            return Response(returnData, status=status.HTTP_409_CONFLICT)


class getQuesApi2(APIView):


    def post(self, request, format=None):


        returnData = getQuestion.getQuestionSetv2(request.data)
        if returnData == '404-1':
            return Response(returnData, status=status.HTTP_404_NOT_FOUND)
        elif returnData == '400-1':
            return Response(returnData, status=status.HTTP_400_BAD_REQUEST)
        elif returnData == '409-1':
            return Response(returnData, status=status.HTTP_409_CONFLICT)
        else:
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
    

class DeleteQues(APIView):


    def post(self, request, format=None):
        returnData = genQuestion.deleteQuestion(request.data)
        if returnData == '404-1':
            return Response(returnData, status=status.HTTP_404_NOT_FOUND)
        elif returnData == '404-2':
            return Response(returnData, status=status.HTTP_404_NOT_FOUND)
        elif returnData == '409-1':
            return Response(returnData, status=status.HTTP_409_CONFLICT)
        else:
            return Response(returnData, status=status.HTTP_202_ACCEPTED)


class FetchServerTime(APIView):


    def post(self, request, format=None):


        returnData = str(datetime.datetime.today())
        return Response(returnData, status=status.HTTP_202_ACCEPTED)


class SetApiPassword(APIView):


    def post(self, request, format=None):


        returnData = apiPassword.setPassword(request.data)
        if returnData == '400':
            return Response(returnData, status=status.HTTP_400_BAD_REQUEST)
        elif returnData == '409-1':
            return Response(returnData, status=status.HTTP_409_CONFLICT)
        else:
            return Response(returnData, status=status.HTTP_202_ACCEPTED)


class ModifyApiPassword(APIView):


    def post(self, request, format=None):


        returnData = apiPassword.modifyPassword(request.data)
        if returnData == '404-2':
            return Response(returnData, status=status.HTTP_404_NOT_FOUND)
        elif returnData == '409-1':
            return Response(returnData, status=status.HTTP_409_CONFLICT)
        else:
            return Response(returnData, status=status.HTTP_202_ACCEPTED)


class DeleteRankingAPI(APIView):


    def post(self, request, format=None):


        returnData = deleteRanking.deletePreviousRank(request.data)
        if returnData == '404-1':
            return Response(returnData, status=status.HTTP_404_NOT_FOUND)
        elif returnData == '404-2':
            return Response(returnData, status=status.HTTP_404_NOT_FOUND)
        elif returnData == '409-1':
            return Response(returnData, status=status.HTTP_409_CONFLICT)
        else:
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
