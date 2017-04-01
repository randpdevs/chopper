from ..models import *
import bcrypt


def setPassword(request):
    try:
        passwordObj = ApiPassword()
    except:
        return '400'
    try:
        ApiPassword.objects.get(apiName=request['apiName'])
        return "409-1"
    except:
        passwordObj.apiName = request['apiName']
        passwordObj.apiPassword = bcrypt.hashpw(str(request['apiPassword']), bcrypt.gensalt())
        passwordObj.save()
        return  '202'

def modifyPassword(request):
    try:
        passwordObj = ApiPassword.objects.get(apiName=request['apiName'])
    except:
        return '404-2'
    if bcrypt.checkpw(str(request['oldPassword']),str(passwordObj.apiPassword)):
        passwordObj.apiPassword = bcrypt.hashpw(str(request['newPassword']), bcrypt.gensalt())
    else:
        return "409-1"
    passwordObj.save()
    return '202'
