from django import template


register = template.Library()



@register.filter(name='placeholder')
def placeholder(value, arg):


	return value.as_widget(attrs={'placeholder': arg})