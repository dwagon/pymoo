from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^game/', include('game.urls')),
    url(r'^api/v1/planet/', include('planet.apiurls')),
    url(r'^api/v1/system/', include('system.apiurls')),
    url(r'^api/v1/game/', include('game.apiurls')),
)
