from django.conf.urls import url

from . import views

app_name = 'login'
urlpatterns = [
    url(r'^register/$', views.userRegisterAPI.as_view()),
    url(r'^login/$', views.userLoginAPI.as_view()),

]