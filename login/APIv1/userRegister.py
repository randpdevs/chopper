from ..models import *
import bcrypt


def userRegister(request):
	userName = request['userName']
	age = request['userAge']
	country = request['userCountry']
	email = request['emailID']
	password = str(request['userPassword'])
	password = bcrypt.hashpw(str(password), bcrypt.gensalt())
	userObj = UserModel()
	userObj.UserName = userName
	userObj.Age = age
	userObj.Country = country
	userObj.EmailID = email
	userObj.Password = password

	try:
		userObj.save()
		userStatObj = UserStat()
		userStatObj.UserName = UserModel.objects.get(UserName = request['userName'])
		userStatObj.save()
		return 202
	except:
		return 400