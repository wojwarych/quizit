from django.shortcuts import render
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import EasyQuest, MediumQuest, HardQuest



def levels(request):


	objects = [EasyQuest, MediumQuest, HardQuest]
	objects_attr = {}
	for _, each in enumerate(objects):

		objects_attr[each.__name__] = each

	questions_selection = {}
	for key, value in objects_attr.items():

		query = objects_attr[key].objects.get_questions()
		questions_selection[key] = query

	for key, value in objects_attr.items():

		request.session[key+'Num'] = questions_selection[key]

	return render(request, 'tennis/levels.html')


def easy(request):


	query_data = request.session.get('EasyQuestNum')
	query = EasyQuest.objects.filter(id__in=query_data)

	paginator = Paginator(query, 1)

	page = request.GET.get('page')

	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		questions = paginator.page(1)
	except EmptyPage:
		questions = paginator.page(paginator.num_pages)

	progress_bar_div = (100//questions.paginator.num_pages)
	progress_bar_list = (
		[x*progress_bar_div for x in range(0, questions.paginator.num_pages)])
	paginate_progress = Paginator(progress_bar_list, 1)
	try:
		view_progress = paginate_progress.page(page)
	except PageNotAnInteger:
		view_progress = paginate_progress.page(1)
	except EmptyPage:
		view_progress = paginator.page(paginator.num_pages)

	context = {
		'chosen_questions': questions,
		'progress_list': view_progress}

	return render(
		request,
		'tennis/questions_level.html',
		context)


def medium(request):


	query_data = request.session.get('MediumQuestNum')
	query = MediumQuest.objects.filter(id__in=query_data)

	paginator = Paginator(query, 1)

	page = request.GET.get('page')

	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		questions = paginator.page(1)
	except EmptyPage:
		questions = paginator.page(paginator.num_pages)

	progress_bar_div = (100//questions.paginator.num_pages)
	progress_bar_list = ([x*progress_bar_div 
		for x in range(0, questions.paginator.num_pages)])
	paginate_progress = Paginator(progress_bar_list, 1)
	try:
		view_progress = paginate_progress.page(page)
	except PageNotAnInteger:
		view_progress = paginate_progress.page(1)
	except EmptyPage:
		view_progress = paginator.page(paginator.num_pages)

	context = {
		'chosen_questions': questions,
		'progress_list': view_progress}

	return render(
		request,
		'tennis/questions_level.html',
		context)


def hard(request):


	query_data = request.session.get('HardQuestNum')
	query = HardQuest.objects.filter(id__in=query_data)

	paginator = Paginator(query, 1)

	page = request.GET.get('page')

	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		questions = paginator.page(1)
	except EmptyPage:
		questions = paginator.page(paginator.num_pages)

	progress_bar_div = (100//questions.paginator.num_pages)
	progress_bar_list = ([x*progress_bar_div 
		for x in range(0, questions.paginator.num_pages)])
	paginate_progress = Paginator(progress_bar_list, 1)
	try:
		view_progress = paginate_progress.page(page)
	except PageNotAnInteger:
		view_progress = paginate_progress.page(1)
	except EmptyPage:
		view_progress = paginator.page(paginator.num_pages)

	context = {
		'chosen_questions': questions,
		'progress_list': view_progress}

	return render(
		request,
		'tennis/questions_level.html',
		context)


def submit(request):


	return HttpResponse("Thank you for answering questions!")