from django.conf.urls import patterns, url

from .views import details

urlpatterns = patterns(
    '',
    url(r'^details/(?P<planet_id>\d+)$', details, name='planetDetails'),
)

# EOF
