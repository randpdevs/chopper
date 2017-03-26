from ..models import UserModel
import bcrypt

def userLogin(request):
    userObject = UserModel.objects.get(UserName=request['userName'])
    if bcrypt.checkpw(str(request['password']),str(userObject.Password)):
        return "Login succeded"
    else:
        return "Wrong password"
