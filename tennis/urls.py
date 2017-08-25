from django.conf.urls import url
from . import views


app_name = 'tennis'
urlpatterns = [
	url(r'^$', views.levels, name='levels'),
	url(r'^easy$', views.easy, name='easy'),
	url(r'^medium$', views.medium, name='medium'),
	url(r'^hard$', views.hard, name='hard'),
	url(r'^submit$', views.submit, name='submit'),
]