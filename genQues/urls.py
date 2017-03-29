from django.conf.urls import url

from . import views

app_name = 'genQues'
urlpatterns = [
    url(r'^genQuest/$', views.genQuesAPI.as_view()),
    url(r'^genQuest1/$', views.genQuesAPI1.as_view()),
    url(r'^getQuest/$', views.getQuesApi.as_view()),
    url(r'^getRanking/$', views.getRankApi.as_view()),
    url(r'^submitRanking/$', views.submitRankApi.as_view()),
    url(r'^getQuest1/$', views.getQuesApi1.as_view()),
    url(r'^getQuest2/$', views.getQuesApi2.as_view()),
    url(r'^genQuestForTomorrow/$', views.genQuesAPIForTomorrow.as_view()),
    url(r'^genQuestForToday/$', views.genQuesAPIForToday.as_view()),
    url(r'^fetchservertime/$', views.FetchServerTime.as_view()),
    url(r'^deleteques/$', views.DeleteQues.as_view()),

]