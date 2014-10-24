from django.conf.urls import patterns, url

from .views import details, assignWorkers, constructBuilding, constructShip

urlpatterns = patterns(
    '',
    url(r'^details/(?P<planet_id>\d+)$', details, name='planetDetails'),
    url(r'^assignWorkers/(?P<planet_id>\d+)/(?P<oldprof>\w+)/(?P<newprof>\w+)$', assignWorkers, name='assignWorkers'),
    url(r'^constructBuilding/(?P<planet_id>\d+)/(?P<build_id>\w+)$', constructBuilding, name='constructBuilding'),
    url(r'^constructShip/(?P<planet_id>\d+)/(?P<design_id>\w+)$', constructShip, name='constructShip'),
)

# EOF
