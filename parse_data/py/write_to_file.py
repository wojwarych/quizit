import sys
import os
import django



with open(sys.argv[1]) as file_read:

	corpus = file_read.readlines()

file_read.close()

corpus_work = corpus.copy()


def save_to_base(model):

			
	for i in corpus:

		try:
			question = corpus_work.pop(0).rstrip('\n\r')
			first = corpus_work.pop(0).rstrip('\n\r')
			second = corpus_work.pop(0).rstrip('\n\r')
			third = corpus_work.pop(0).rstrip('\n\r')
			fourth = corpus_work.pop(0).rstrip('\n\r')
			good_answ = int(corpus_work.pop(0).rstrip('\n\r'))

			new_entry = (model(
				question=question, first_answ=first, second_answ=second,
				third_answ=third, fourth_answ=fourth, good_answ=good_answ).save())
		
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

	from tennis.models import EasyQuest, MediumQuest, HardQuest
	
	if sys.argv[2] == 'EasyQuest':
		save_to_base(EasyQuest)

	elif sys.argv[2] == 'MediumQuest':
		save_to_base(MediumQuest)

	else:
		save_to_base(HardQuest)
