from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from examples.api.views import ExampleOneViewSet

router = routers.DefaultRouter()
router.register(r'example_ones', ExampleOneViewSet, basename='example_one')

urlpatterns = [
    url(r'', include(router.urls)),
]
