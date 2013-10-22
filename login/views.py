from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import re

def index(request):
	allowed_methods = ['get','post','put','delete','options']
	if request.META['REQUEST_METHOD'] == 'OPTIONS':
		response = HttpResponse()
		response['allow'] = ','.join([allowed_methods])
		return response
	if request.META['REQUEST_METHOD'] == 'GET':
		return render(request,'login/index.html')

	have_error = False

	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']
	retype_password = request.POST['verify']
	username_error = email_error = password_error = None

	params = {'username':username,
				'email':email}

	if not valid_username(username):
		params['username_error'] = "That's not a valid username."
		have_error = True

	if not valid_email(email):
		params['email_error'] = "That's not a valid email."
		have_error = True

	if not valid_password(password):
		params['password_error'] = "That wasn't a valid password."
		have_error = True
	elif password != retype_password:
		params['password_error'] = "Your passwords didn't match."
		have_error = True

	if have_error:
		return render(request, 'login/index.html', params)
	return HttpResponseRedirect(reverse('login:welcome')+"?username="+str(username))

def login(request):
	return HttpResponse("<h1>welcome "+request.GET['username']+"!</h1>")

def valid_username(username):
	USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
	return USER_RE.match(username)

def valid_email(email):
	EMAIL_RE = re.compile(r'^^[\S]+@[\S]+\.[\S]+$')
	return EMAIL_RE.match(email)

def valid_password(password):
	PASSWORD_RE = re.compile(r'^.{3,20}$')
	return PASSWORD_RE.match(password)
