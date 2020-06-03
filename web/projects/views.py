from django.views import generic
from .models import Project

class IndexView(generic.ListView):
    model = Project
    template_name = 'projects/index.html'
