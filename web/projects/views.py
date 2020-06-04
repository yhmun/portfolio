from django.views import generic
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer

class IndexView(generic.ListView):
    model = Project
    template_name = 'projects/index.html'


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
