from django.forms.widgets import TextInput


class CustomTextInput(TextInput):


	template_name = 'tennis/widget_template.html'