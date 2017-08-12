from django.shortcuts import render
from django.http import HttpResponse
from .models import Tennis

# Create your views here.
def index(request):


	return render(request, 'tennis/index.html')


def levels(request):


	return render(request, 'tennis/levels.html')


def easy(request):

	chosen_questions = Tennis.objects.all()
	return render(request, "tennis/easy.html", {'chosen_questions': chosen_questions})


def medium(request):


	return HttpResponse("Medium test!")


def hard(request):


	return HttpResponse("Hard test!")