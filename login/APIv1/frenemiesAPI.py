from ..models import *


def addFriend(request):
    try:
        userObj = UserModel.objects.get(UserName = request['userName'])
    except:
        return '404-1'
    try:
        friendObj = UserModel.objects.get(UserName = request['friendName'])
    except Exception as e :
        return '404'
    userObj.UserFriends.add(friendObj)
    userObj.save()
    return '202'


def getFriendInfo(request):
    try:
        userObj = UserModel.objects.get(UserName = request['userName'])
    except:
        return '404-1'
    senddata = []
    for userFriend in userObj.UserFriends.all():
        senddata.append({"friendName":userFriend.UserName,"Score":userFriend.UserScore})
    return senddata