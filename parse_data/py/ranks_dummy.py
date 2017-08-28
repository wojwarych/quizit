import sys
import os
import django



with open(sys.argv[1]) as file_read:

	corpus = file_read.readlines()

file_read.close()

corpus_work = corpus.copy()


def save_to_base(level, model):

			
	for i in corpus:

		if level == "easy":

			try:
				user = corpus_work.pop(0).rstrip('\n\r')
				score = corpus_work.pop(0).rstrip('\n\r')

				new_entry = (model.objects.create(
					username=user, easyquest=score))

			except IndexError as e:
				print(e)
				break

		elif level == "medium":

			try:
				user = corpus_work.pop(0).rstrip('\n\r')
				score = corpus_work.pop(0).rstrip('\n\r')

				new_entry = (model.objects.create(
					username=user, mediumquest=score))
		
			except IndexError as e:
				print(e)
				break

		else:

			try:
				user = corpus_work.pop(0).rstrip('\n\r')
				score = corpus_work.pop(0).rstrip('\n\r')

				new_entry = (model.objects.create(
					username=user, hardquest=score))
			
			except IndexError as e:
				print(e)
				break

	return new_entry

if __name__ == "__main__":

	script_path = os.path.dirname(__file__)
	project_dir = os.path.abspath(os.path.join(script_path,'..','..', '..', 'quizit'))
	sys.path.insert(0, project_dir)
	os.environ['DJANGO_SETTINGS_MODULE'] = 'quizit.settings'

	django.setup()

	
	if sys.argv[2] == "tennis":
		from ranking.models import RankingTennis
		model = RankingTennis

	elif sys.argv[2] == "music":
		from ranking.models import RankingMusic
		model = RankingMusic

	else:
		from ranking.models import RankingLiterature
		model = RankingLiterature

	if sys.argv[3] == 'easy':
		save_to_base(sys.argv[3], model)

	elif sys.argv[3] == 'medium':
		save_to_base(sys.argv[3], model)

	else:
		save_to_base(sys.argv[3], model)