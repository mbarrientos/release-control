from rest_framework import viewsets, serializers

from core.models import Release, Project


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ('commit_id',)


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description')


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
