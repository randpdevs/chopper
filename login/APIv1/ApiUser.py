from ..models import UserModel


def check(request):
    try:
        userObj=UserModel.objects.get(UserName=request['userName'])
        #Found
        return 202
    except:
        #NotFound
        return 400
