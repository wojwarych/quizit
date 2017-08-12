from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^example/', views.example_page, name='example_page'),
	url(r'^about/', views.about, name='about'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^quizes/', views.quizes, name='quizes')
]