from django.conf.urls import url
from . import views



app_name = 'home'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^quizes/$', views.quizes, name='quizes'),
	url(r'^posts/(?P<post_id>\d+)/$', views.post, name='post'),
	url(r'^msg/$', views.send_msg, name='send_msg')
]