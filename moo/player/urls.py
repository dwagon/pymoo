from django.conf.urls import patterns, url

from .views import details

urlpatterns = patterns(
    '',
    url(r'^details/(?P<player_id>\d+)$', details, name='playerDetails'),
)

# EOF
