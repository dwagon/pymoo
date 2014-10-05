from django.conf.urls import patterns, url

from .views import details

urlpatterns = patterns(
    '',
    url(r'^details/(?P<ship_id>\d+)$', details, name='shipDetails'),
)

# EOF
