from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'Theatre_CS399.views.home', name='home'),
	url(r'^movies$', 'Theatre_CS399.views.movies', name='movies'),
	url(r'^performances$', 'Theatre_CS399.views.performances', name='performances'),
	url(r'^store$', 'Theatre_CS399.views.store', name='store'),
	url(r'^location$', 'Theatre_CS399.views.location', name='location'),
	
    url(r'^admin/', include(admin.site.urls)),
)
