from django.shortcuts import render
from .models import model3d

def homepage(request):
  glbs=model3d.objects.all
  return render(request, 'index.html', {'glbs':glbs})