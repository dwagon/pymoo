from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
import restviews

urlpatterns = [
    url(
        r'',
        include([
            url(r'^$', restviews.ShipList.as_view()),
            url(r'^(?P<pk>[0-9]+)/$', restviews.ShipDetail.as_view()),
        ])
    )
]

urlpatterns = format_suffix_patterns(urlpatterns)

# EOF
