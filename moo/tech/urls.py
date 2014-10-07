from django.conf.urls import patterns, url

from .views import details

urlpatterns = patterns(
    '',
    url(r'^details/(?P<tech_id>\d+)$', details, name='techDetails'),
)

# EOF
