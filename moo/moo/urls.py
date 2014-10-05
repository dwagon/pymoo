from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import index

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^game/', include('game.urls')),
    url(r'^planet/', include('planet.urls')),
    url(r'^player/', include('player.urls')),
    url(r'^ship/', include('ship.urls')),
    url(r'^system/', include('system.urls')),

    url(r'^api/v1/game/', include('game.apiurls')),
    url(r'^api/v1/planet/', include('planet.apiurls')),
    url(r'^api/v1/system/', include('system.apiurls')),
)
