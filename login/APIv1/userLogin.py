from ..models import UserModel
import bcrypt

def userLogin(request):
    try:
        userObject = UserModel.objects.get(UserName=request['userName'])
        if bcrypt.checkpw(str(request['password']),str(userObject.Password)):
            returnData={}
            returnData['UserName']=userObject.UserName
            returnData['EmailID']=userObject.EmailID
            returnData['Age'] = userObject.Age
            returnData['Country'] = userObject.Country

            return returnData
        else:
            return 400
    except:
        return 404