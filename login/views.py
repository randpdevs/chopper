from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import responses
import json
import time,threading
from APIv1 import userRegister, userLogin,ApiUser, frenemiesAPI, userStatAPI
# Create your views here.

class userRegisterAPI(APIView):
    def post(self, request, format=None):
        returnData =  userRegister.userRegister(request.data)
        return Response(returnData, status=status.HTTP_202_ACCEPTED)

class userLoginAPI(APIView):
    def post(self, request, format=None):
        returnData = userLogin.userLogin(request.data)
        return Response(returnData, status=status.HTTP_202_ACCEPTED)

class CheckUserNameAPI(APIView):
    def post(self, request, format=None):
        returnData = ApiUser.check(request.data)
        return Response(returnData, status=status.HTTP_202_ACCEPTED)


class AddFreindAPI(APIView):
    def post(self, request, format=None):
        returnData = frenemiesAPI.addFriend(request.data)
        if returnData != '404':
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(returnData, status=status.HTTP_404_NOT_FOUND)

class GetFriendInfoAPI(APIView):
    def post(self, request, format =None):
        returnData = frenemiesAPI.getFriendInfo(request.data)
        if returnData != '404-1':
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(returnData, status=status.HTTP_404_NOT_FOUND)


class GetUserStat(APIView):
    def post(self, request, format=None):
        returnData = userStatAPI.gettUserStat(request.data)
        if returnData == '404':
            return Response(returnData, status=status.HTTP_404_NOT_FOUND)
        elif returnData == '400':
            return Response(returnData, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(returnData, status=status.HTTP_202_ACCEPTED)