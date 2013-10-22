from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse

def index(request):
	if request.META['REQUEST_METHOD'] == 'GET':
		return render(request,'rot13/index.html')
	if request.META['REQUEST_METHOD'] == 'POST':
		plaintext = request.POST['text']
		encrypted = ''
		for char in plaintext:
			encryptedChar = char.lower()
			if encryptedChar.isalpha():
				encryptedChar = chr((ord(encryptedChar)%ord('a')+13)%26+97)
			if char.isupper():
				encryptedChar = encryptedChar.upper()
			encrypted = encrypted + encryptedChar
		return render_to_response('rot13/index.html', {
			'encrypted': encrypted, 
			'csrf_token':request.POST['csrfmiddlewaretoken']})