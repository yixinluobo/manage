from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^login/$', views.LoginAPI.as_view()),
]