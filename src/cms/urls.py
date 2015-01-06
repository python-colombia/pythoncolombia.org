# Django Modules
from django.conf.urls import *

urlpatterns = patterns(
    'cms.views',
    url(r'^$', 'index', name='index'),
)
