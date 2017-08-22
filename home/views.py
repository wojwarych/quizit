from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import News
from .forms import ContactForm

from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template



def index(request):

	query = News.objects.order_by('-pub_date')[:5]

	context = {'news': query}
	return render(request, 'home/index.html', context)


def example_page(request):


	return render(request, 'home/example_page.html')


def about(request):


	return render(request, 'home/about.html')


def contact(request):


	contact_form = ContactForm

	if request.method == 'POST':
		form = contact_form(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('name', '')
			contact_email = request.POST.get('email', '')
			content = request.POST.get('message', '')

			template = get_template('contact_template.txt')
			context = {
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': content,
			}
			content = template.render(context)

			email = EmailMessage(
				"New contact form submission",
				content,
				"Your website" +'',
				['woj.warych@gmail.com'],
				headers = {'Reply-To': contact_email }
			)
			email.send()
			return redirect('home:contact')


	return render(request, 'home/contact.html', {'form': contact_form})


def quizes(request):


	return render(request, 'home/quiz_nav.html')


def post(request, post_id):


	the_post = News.objects.get(id=post_id)
	context = {'post': the_post}


	return render(request, 'home/post.html', context)

