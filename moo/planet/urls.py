from django.conf.urls import patterns, url

from .views import details, assignWorkers

urlpatterns = patterns(
    '',
    url(r'^details/(?P<planet_id>\d+)$', details, name='planetDetails'),
    url(r'^assignWorkers/(?P<planet_id>\d+)/(?P<oldprof>\w+)/(?P<newprof>\w+)$', assignWorkers, name='assignWorkers'),
)

# EOF
