from django.shortcuts import render
from django.http import HttpResponse


def index(request):


	return render(request, 'home/index.html')


def example_page(request):


	return render(request, 'home/example_page.html')


def about(request):


	return render(request, 'home/about.html')


def contact(request):


	return render(request, 'home/contact.html')


def quizes(request):


	return render(request, 'home/quiz_nav.html')