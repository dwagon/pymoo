from django.conf.urls import patterns, url

from .views import details

urlpatterns = patterns(
    '',
    url(r'^details/(?P<system_id>\d+)$', details, name='systemDetails'),
)

# EOF
