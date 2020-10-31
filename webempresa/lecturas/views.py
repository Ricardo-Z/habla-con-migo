from django.shortcuts import render, get_object_or_404
from .models import Lectura

# Create your views here.
def lectura(request):
     posts = Lectura.objects.all()
     return render(request, "lecturas/lectura.html" , {'posts': posts})