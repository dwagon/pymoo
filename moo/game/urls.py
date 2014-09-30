from django.conf.urls import patterns, url

from .views import makeGalaxy

urlpatterns = patterns(
    '',
    url(r'^$', makeGalaxy, name='makeGalaxy'),
)

# EOF
