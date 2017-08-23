from django.forms import ModelForm
from .models import EasyQuest, MediumQuest, HardQuest


class EasyForm(ModelForm):
	class Meta:
		model = EasyQuest
		fields = (
			'question', 
			'first_answ', 
			'second_answ', 
			'third_answ', 
			'fourth_answ')
		