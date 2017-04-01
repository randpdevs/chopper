from ..models import  *
import bcrypt

def deletePreviousRank(request):
    try:
        apiPass = ApiPassword.objects.get(apiName = 'deletePreviousRank')
    except:
        return "404-1"

    if bcrypt.checkpw(str(request['password']), str(apiPass)):
        try:
            rankingObj = rankingSet().objects.filter(questionA = request['questionID'])
            rankingObj.delete()
            return '202-1'
        except Exception as e:
            return '404-2'
    else:
        return "409-1"
