from django.conf.urls import url

from core.views import ReleaseListView

urlpatterns = [
    url(r'', ReleaseListView.as_view())
]
