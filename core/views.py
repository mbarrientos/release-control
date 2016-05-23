from django.views.generic import ListView

from core.models import Release


class ReleaseListView(ListView):

    model = Release