from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)

app_name = 'projects'
urlpatterns = [    
    path('projects/', views.IndexView.as_view(), name='index'),
    path('api/v1/', include(router.urls)),
]