from django.conf.urls import url

from . import views

app_name = 'genQues'
urlpatterns = [
    url(r'^getquestion/$', views.getQuesApi2.as_view()),
    url(r'^getranking/$', views.getRankApi.as_view()),
    url(r'^submitranking/$', views.submitRankApi.as_view()),
    url(r'^genquestfortomorrow/$', views.genQuesAPIForTomorrow.as_view()),
    url(r'^genquestfortoday/$', views.genQuesAPIForToday.as_view()),
    url(r'^fetchservertime/$', views.FetchServerTime.as_view()),
    url(r'^deleteques/$', views.DeleteQues.as_view()),
    url(r'^setapipassword/$', views.SetApiPassword.as_view()),
    url(r'^modifyapipassword/$', views.ModifyApiPassword.as_view()),
    url(r'^deleterankingset/$', views.DeleteRankingAPI.as_view()),

]