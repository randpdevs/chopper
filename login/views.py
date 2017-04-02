from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import responses
import json
import time,threading
from APIv1 import userRegister, userLogin,ApiUser
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
