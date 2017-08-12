from django.conf.urls import url
from . import views

app_name = 'tennis'
urlpatterns = [
	url(r'^$', views.levels, name='levels'),
	url(r'^levels/easy$', views.easy, name='easy'),
	url(r'^levels/medium$', views.medium, name='medium'),
	url(r'^levels/hard$', views.hard, name='hard'),
]