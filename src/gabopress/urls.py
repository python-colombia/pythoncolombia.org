# Django Modules
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns(
    '',
    url(r'^$', include('cms.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
# Includes static urls settings to main urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Includes media urls settings to main urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
