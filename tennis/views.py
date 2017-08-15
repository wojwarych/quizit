from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Tennis


def levels(request):


	return render(request, 'tennis/levels.html')


def easy(request):


	chosen_questions = Tennis.objects.all()
	paginator = Paginator(chosen_questions, 1)

	page = request.GET.get('page')

	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		questions = paginator.page(1)
	except EmptyPage:
		questions = paginator.page(paginator.num_pages)

	progress_bar_div = (100//questions.paginator.num_pages)
	progress_bar_list = [x*progress_bar_div for x in range(0, 4)]
	paginate_progress = Paginator(progress_bar_list, 1)
	try:
		view_progress = paginate_progress.page(page)
	except PageNotAnInteger:
		view_progress = paginate_progress.page(1)
	except EmptyPage:
		view_progress = paginator.page(paginator.num_pages)

	return render(request, "tennis/easy.html", {'chosen_questions': questions, 'progress_list': view_progress})


def medium(request):


	return HttpResponse("Medium test!")


def hard(request):


	return HttpResponse("Hard test!")


def submit(request):


	return HttpResponse("Thank you for answering questions!")