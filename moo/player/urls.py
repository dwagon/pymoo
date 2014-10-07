from django.conf.urls import patterns, url

from .views import details, setResearch

urlpatterns = patterns(
    '',
    url(r'^details/(?P<player_id>\d+)$', details, name='playerDetails'),
    url(r'^setResearch/(?P<player_id>\d+)/(?P<tech_id>\d+)$', setResearch, name='setResearch'),
)

# EOF
