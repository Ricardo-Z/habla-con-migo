
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lectura, name="lectura"),
]