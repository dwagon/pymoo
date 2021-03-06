from django.conf.urls import patterns, url

from .views import new, details, delete, nextTurn

urlpatterns = patterns(
    '',
    url(r'^details/(?P<game_id>\d+)$', details, name='gameDetails'),
    url(r'^delete/(?P<game_id>\d+)$', delete, name='gameDelete'),
    url(r'^new/(?P<size>\w+)$', new, name='gameNew'),
    url(r'^turn/(?P<game_id>\d+)$', nextTurn, name='nextTurn'),
)

# EOF
