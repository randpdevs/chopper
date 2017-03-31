from ..models import  *
import bcrypt

def deletePreviousRank(request):
    try:
        apiPass = ApiPassword.objects.get(apiName = 'deletePreviousRank')
    except:
        return "api is not password protected"

    if bcrypt.checkpw(str(request['password']), str(apiPass)):
        try:
            rankingObj = rankingSet().objects.filter(questionA = request['questionID'])
            rankingObj.delete()
        except Exception as e:
            return '400'
    else:
        return "wrong password"


