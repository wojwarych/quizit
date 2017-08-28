from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.db.utils import IntegrityError

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import EasyQuest, MediumQuest, HardQuest
from .forms import EasyForm, MediumForm, HardForm, NameForm
from ranking.models import RankingLiterature


"""FUNCTIONS USED IN VIEWS"""
def collect_answer(request):


	if "question-option" in request.POST:

		request.session['choice'] = (
		request.POST.get("question-option", ""))

		request.session['user_answers'].append(request.session['choice'])



def compare_results(request):

	score = 0
	good_answ = 0
	
	answ_transform = request.session['user_answers']
	for index, value in enumerate(answ_transform):

		answ_transform[index] = int(value)

	for index, value in enumerate(answ_transform):

		if answ_transform[index] == request.session['answers'][index]:

			good_answ += 1

			if request.session['undergo_test'] == "Easy":
				
				score += 2
			
			elif request.session['undergo_test'] == "Medium":

				score += 4

			else:

				score += 6

	request.session['points'] = score
	request.session['final_answers'] = good_answ


def create_quiz(request, database, level_db_session):


	query_data = request.session.get(level_db_session)
	query = database.objects.filter(id__in=query_data)
	request.session['answers'] = list(query.values_list('good_answ', flat=True))

	return query



def paginate_query(request, query, num=1):


	paginator = Paginator(query, num)
	page = request.GET.get('page')

	try:
		
		questions = paginator.page(page)
		
	except PageNotAnInteger:
		
		questions = paginator.page(1)
		
	except EmptyPage:
		
		questions = paginator.page(paginator.num_pages)

	return questions, page



def paginate_progress_bar(related_questions, page, num=1):


	bar_division = (100//related_questions.paginator.num_pages)
	values_list = (
		[x*bar_division for x in range(0, related_questions.paginator.num_pages)])
	paginate_progress = Paginator(values_list, num)

	try:
		view_progress = paginate_progress.page(page)
		
	except PageNotAnInteger:
		view_progress = paginate_progress.page(1)
		
	except EmptyPage:
		view_progress = paginator.page(paginator.num_pages)

	return view_progress



"""VIEWS"""
def levels(request):

	if request.method == 'GET':

		request.session['choice'] = ""
		request.session['final_answers'] = ""
		request.session['points'] = ""
		request.session['undergo_test'] = ""
		request.session['username'] = ""
		
		user_answers = []
		request.session['user_answers'] = user_answers


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

	return render(request, 'literature/levels.html')



def easy(request):


	FormSet = modelformset_factory(EasyQuest, form=EasyForm, extra=0)
	request.session['undergo_test'] = 'Easy'

	if request.method == 'GET':
		
		query = create_quiz(request, EasyQuest, 'EasyQuestNum')

		questions, page = paginate_query(request, query)

		view_progress = paginate_progress_bar(questions, page)
	
		page_query = query.filter(id__in=[question.id for question in questions])
		
		formset = FormSet(queryset=page_query)

		
		context = {
			'chosen_questions': questions,
			'formset': formset,
			'progress_list': view_progress}
		
		return render(request, 'literature/questions_level.html', context)

	else:

		form = FormSet(request.POST, request.FILES)
		# Your validation and rest of the 'POST' code

		if form.is_valid():

			collect_answer(request)

			query = create_quiz(request, EasyQuest, 'EasyQuestNum')

			questions, page = paginate_query(request, query)

			view_progress = paginate_progress_bar(questions, page)

			page_query = query.filter(id__in=[question.id for question in questions])
		
			formset = FormSet(queryset=page_query)

			context = {
			'chosen_questions': questions,
			'formset': formset,
			'progress_list': view_progress}

			return render(request, 'literature/questions_level.html', context)



def medium(request):


	FormSet = modelformset_factory(MediumQuest, form=MediumForm, extra=0)
	request.session['undergo_test'] = 'Medium'

	if request.method == 'GET':
		
		query = create_quiz(request, MediumQuest, 'MediumQuestNum')

		questions, page = paginate_query(request, query)

		view_progress = paginate_progress_bar(questions, page)
	
		page_query = query.filter(id__in=[question.id for question in questions])
		
		formset = FormSet(queryset=page_query)

		
		context = {
			'chosen_questions': questions,
			'formset': formset,
			'progress_list': view_progress}
		
		return render(request, 'literature/questions_level.html', context)

	else:

		form = FormSet(request.POST, request.FILES)
		# Your validation and rest of the 'POST' code

		if form.is_valid():

			collect_answer(request)

			query = create_quiz(request, MediumQuest, 'MediumQuestNum')

			questions, page = paginate_query(request, query)

			view_progress = paginate_progress_bar(questions, page)

			page_query = (
				query.filter(id__in=[question.id for question in questions]))
		
			formset = FormSet(queryset=page_query)

			context = {
			'chosen_questions': questions,
			'formset': formset,
			'progress_list': view_progress}

			return render(request, 'literature/questions_level.html', context)



def hard(request):


	FormSet = modelformset_factory(HardQuest, form=HardForm, extra=0)
	request.session['undergo_test'] = 'Hard'

	if request.method == 'GET':
		
		query = create_quiz(request, HardQuest, 'HardQuestNum')

		questions, page = paginate_query(request, query)

		view_progress = paginate_progress_bar(questions, page)
	
		page_query = (
			query.filter(id__in=[question.id for question in questions]))
		
		formset = FormSet(queryset=page_query)

		
		context = {
			'chosen_questions': questions,
			'formset': formset,
			'progress_list': view_progress}
		
		return render(request, 'literature/questions_level.html', context)

	else:

		form = FormSet(request.POST, request.FILES)
		# Your validation and rest of the 'POST' code

		if form.is_valid():

			collect_answer(request)

			query = create_quiz(request, HardQuest, 'HardQuestNum')

			questions, page = paginate_query(request, query)

			view_progress = paginate_progress_bar(questions, page)

			page_query = (
				query.filter(id__in=[question.id for question in questions]))
		
			formset = FormSet(queryset=page_query)

			context = {
			'chosen_questions': questions,
			'formset': formset,
			'progress_list': view_progress}

			return render(request, 'literature/questions_level.html', context)



def submit(request):


	if request.method == 'POST':

		collect_answer(request)

		compare_results(request)

		form = NameForm(request.POST)
		# check whether it's valid:
		if form.is_valid():

			request.session['username'] = form.cleaned_data['username']

			if request.session['undergo_test'] == 'Easy':
				
				try:	
					new_score = RankingLiterature.objects.create(
						username=request.session['username'],
						easyquest=request.session['points'])

				except IntegrityError as e:
					return render(request, 'home/base.html', {"message": e.message})

			elif request.session['undergo_test'] == 'Medium':

				try:
					new_score = RankingLiterature.objects.create(
						username=request.session['username'],
						mediumquest=request.session['points'])

				except IntegrityError as e:
					return render(request, 'home/base.html', {"message": e.message})

			else:

				try:
					new_score = RankingLiterature.objects.create(
						username=request.session['username'],
						mediumquest=request.session['points'])

				except IntegrityError as e:
					return render(request, 'home/base.html', {"message": e.message})

			return redirect('ranking:ranking')

	else:
		form = NameForm()

	return render(request, 'literature/add_score.html', {'form': form})
