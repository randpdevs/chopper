from ..models import UserModel
import bcrypt

def userLogin(request):
    try:
        userObject = UserModel.objects.get(UserName=request['userName'])
        if bcrypt.checkpw(str(request['password']),str(userObject.Password)):
            return 202
        else:
            return 400
    except:
        return 404