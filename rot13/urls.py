from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$','rot13.views.index', name='index'),
	)