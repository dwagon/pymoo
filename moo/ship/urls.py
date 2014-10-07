from django.conf.urls import patterns, url

from .views import details, setDestination

urlpatterns = patterns(
    '',
    url(r'^details/(?P<ship_id>\d+)$', details, name='shipDetails'),
    url(r'^setDestination/(?P<ship_id>\d+)/(?P<dest_id>\d+)$', setDestination, name='setDestination'),
)

# EOF
