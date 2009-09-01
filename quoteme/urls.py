from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^quotes/(?P<slug>[-\w]+)/$', 'quoteme.views.quote_detail', name='quote_detail'),
    url(r'^quotes/$', 'quoteme.views.quote_list', name='quote_list'),

    url(r'^testimonials/$', 'quoteme.views.testimonial_list', name='testimonial_list'),

    url(r'^$', direct_to_template, {'template':'example_home.html'}),
    (r'^admin/(.*)', admin.site.root),
)