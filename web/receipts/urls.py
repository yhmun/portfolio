from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path("receipt_json/", views.receipt_json),
]