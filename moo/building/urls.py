from django.conf.urls import patterns, url

from .views import details

urlpatterns = patterns(
    '',
    url(r'^details/(?P<building_id>\d+)$', details, name='buildingDetails'),
)

# EOF
