from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
import restviews

urlpatterns = [
    url(
        r'',
        include([
            url(r'^$', restviews.SystemList.as_view()),
            url(r'^(?P<pk>[0-9]+)/$', restviews.SystemDetail.as_view()),
            url(r'category$', restviews.SystemCategoryList.as_view()),
            url(r'^category/(?P<pk>[0-9]+)/$', restviews.SystemCategoryDetail.as_view()),
        ])
    )
]

urlpatterns = format_suffix_patterns(urlpatterns)

# EOF
