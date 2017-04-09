from django.conf.urls import url

from . import views

app_name = 'login'
urlpatterns = [
    url(r'^register/$', views.userRegisterAPI.as_view()),
    url(r'^login/$', views.userLoginAPI.as_view()),
    url(r'^checkusername/$', views.CheckUserNameAPI.as_view()),
    url(r'^addfriend/$', views.AddFreindAPI.as_view()),
    url(r'^getfriendinfo/$', views.GetFriendInfoAPI.as_view()),
    url(r'^getuserstats/$', views.GetUserStat.as_view()),

]