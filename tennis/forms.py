from django import forms
from django.forms import ModelForm, TextInput, RadioSelect
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
			'first_answ': TextInput(attrs={'type': 'radio'}),
			'second_answ': TextInput(attrs={'type': 'radio'}),
			'third_answ': TextInput(attrs={'type': 'radio'}),
			'fourth_answ': TextInput(attrs={'type': 'radio'}),
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
			'first_answ': TextInput(attrs={'type': 'radio'}),
			'second_answ': TextInput(attrs={'type': 'radio'}),
			'third_answ': TextInput(attrs={'type': 'radio'}),
			'fourth_answ': TextInput(attrs={'type': 'radio'}),
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
			'first_answ': TextInput(attrs={'type': 'radio'}),
			'second_answ': TextInput(attrs={'type': 'radio'}),
			'third_answ': TextInput(attrs={'type': 'radio'}),
			'fourth_answ': TextInput(attrs={'type': 'radio'}),
			}