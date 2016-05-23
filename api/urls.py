from django.conf.urls import include, url
from rest_framework import routers

from api.views import ReleaseViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register(r'release', ReleaseViewSet)
router.register(r'project', ProjectViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
