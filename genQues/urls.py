from django.conf.urls import url

from . import views

app_name = 'genQues'
urlpatterns = [
    url(r'^genQuest/$', views.genQuesAPI.as_view()),
    url(r'^genQuest1/$', views.genQuesAPI1.as_view()),
    url(r'^getQuest/$', views.getQuesApi.as_view()),
    url(r'^getRanking/$', views.getRankApi.as_view()),
    url(r'^submitRanking/$', views.submitRankApi.as_view()),

]