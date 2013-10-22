from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^$','login.views.index', name='home'),
	url(r'^welcome/$','login.views.login', name='welcome')
	)