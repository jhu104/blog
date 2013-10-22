from django.conf.urls import patterns, include, url
from blog import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^testform','blog.views.testHandler', name='testHandler'),
    url(r'^result','blog.views.result', name='result'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': '/home3/jialiang/blog/static'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^rot13/', include('rot13.urls', namespace="rot13")),
    url(r'^login/', include('login.urls', namespace='login')),
)
