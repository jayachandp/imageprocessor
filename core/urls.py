from django.conf.urls import url
from .views import ProcessImageView, ImageDetailView

app_name = 'core'

urlpatterns = [
    url(r'^$', ProcessImageView.as_view(), name='process_image'),
    url(
        r'^(?P<image_id>[^/]+)/$',
        ImageDetailView.as_view(), name='image_detail'
    ),
]
