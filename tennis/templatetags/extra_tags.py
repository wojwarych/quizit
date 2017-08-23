from django import template


register = template.Library()



@register.filter(name='type')
def type(value, arg):


	return value.as_widget(attrs={'type': arg})