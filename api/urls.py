from django.conf.urls import url
from api import views

urlpatterns = [
	url(r'^todos/?$', views.TodoIndex.as_view()),
	url(r'^todos/(?P<pk>[0-9]+)/?$', views.TodoDetail.as_view()),	
	url(r'^dayentries/?$', views.TodoListIndex.as_view()),
	url(r'^dayentries/(?P<pk>[0-9]+)/?$', views.TodoListDetail.as_view()),
]