from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'api/getBooks', 'main.api.get_books'),
    url(r'^admin/', include(admin.site.urls)),
)