from ..models import *
import bcrypt


def setPassword(request):
    passwordObj = ApiPassword()
    try:
        ApiPassword.objects.get(apiName=request['apiName'])
        return "password already set"
    except:
        passwordObj.apiName = request['apiName']
        passwordObj.apiPassword = bcrypt.hashpw(str(request['apiPassword']), bcrypt.gensalt())
        passwordObj.save()
        return  '202'

def modifyPassword(request):
    try:
        passwordObj = ApiPassword.objects.get(apiName=request['apiName'])
        if bcrypt.checkpw(str(request['oldPassword']),str(passwordObj.apiPassword)):
            passwordObj.apiPassword = bcrypt.hashpw(str(request['newPassword']), bcrypt.gensalt())
        else:
            return "419-1"
        passwordObj.save()
        return '202'
    except Exception as e:
        return '404'