from django.conf.urls import patterns, url

from .views import makeGalaxy, details

urlpatterns = patterns(
    '',
    url(r'^details/(?P<game_id>\d+)$', details, name='gameDetails'),
    url(r'^new$', makeGalaxy, name='makeGalaxy'),
)

# EOF
