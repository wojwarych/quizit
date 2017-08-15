from django.conf.urls import url
from . import views


app_name = 'tennis'
urlpatterns = [
	url(r'^$', views.levels, name='levels'),
	url(r'^level/easy$', views.easy, name='easy'),
	url(r'^level/medium$', views.medium, name='medium'),
	url(r'^level/hard$', views.hard, name='hard'),
	url(r'^thank$', views.submit, name='submit'),
]