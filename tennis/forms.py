from django import forms
from django.forms import ModelForm
from .widgets.widget import CustomTextInput
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
		labels = {
			'first_answ': "question-option",
			'second_answ': "question-option",
			'third_answ': "question-option",
			'fourth_answ': "question-option",
		}		
		widgets = {
			'first_answ': CustomTextInput(attrs={'type': 'radio', 'value': '1'}),
			'second_answ': CustomTextInput(attrs={'type': 'radio', 'value': '2'}),
			'third_answ': CustomTextInput(attrs={'type': 'radio', 'value': '3'}),
			'fourth_answ': CustomTextInput(attrs={'type': 'radio', 'value': '4'}),
			}



class MediumForm(ModelForm):


	class Meta:
		model = MediumQuest
		fields = (
			'question', 
			'first_answ', 
			'second_answ', 
			'third_answ', 
			'fourth_answ')
		labels = {
			'first_answ': "question-option",
			'second_answ': "question-option",
			'third_answ': "question-option",
			'fourth_answ': "question-option",
		}		
		widgets = {
			'first_answ': CustomTextInput(attrs={'type': 'radio', 'value': '1'}),
			'second_answ': CustomTextInput(attrs={'type': 'radio', 'value': '2'}),
			'third_answ': CustomTextInput(attrs={'type': 'radio', 'value': '3'}),
			'fourth_answ': CustomTextInput(attrs={'type': 'radio', 'value': '4'}),
			}



class HardForm(ModelForm):


	class Meta:
		model = HardQuest
		fields = (
			'question', 
			'first_answ', 
			'second_answ', 
			'third_answ', 
			'fourth_answ')
		labels = {
			'first_answ': "question-option",
			'second_answ': "question-option",
			'third_answ': "question-option",
			'fourth_answ': "question-option",
		}		
		widgets = {
			'first_answ': CustomTextInput(attrs={'type': 'radio', 'value': '1'}),
			'second_answ': CustomTextInput(attrs={'type': 'radio', 'value': '2'}),
			'third_answ': CustomTextInput(attrs={'type': 'radio', 'value': '3'}),
			'fourth_answ': CustomTextInput(attrs={'type': 'radio', 'value': '4'}),
			}