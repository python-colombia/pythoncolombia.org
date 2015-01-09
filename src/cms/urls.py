# Django Modules
from django.conf.urls import *

urlpatterns = patterns(
    'cms.views',
    url(r'^$', 'index', name='index'),
    url(r'^article/(?P<slug>[\w-]+)/$', 'article', name='view_article'),
    url(r'^(?P<year>\d{4})/$', 'articles', name="year_archive"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'articles', name="month_archive"),
    url(r'^tag/(?P<tag>[\w-]+)/$', 'articles', name='tag_archive'),
    url(r'^author/(?P<author>[\w-]+)/$', 'articles', name='author_archive'),
    url(r'^confirm/comment/$', 'comment_posted', name='comment_posted'),
    url(r'^post/(?P<slug>[\w-]+)/$', 'view_post', name='view_post'),
)
