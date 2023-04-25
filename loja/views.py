from django.shortcuts import render
from django.http import HttpResponse
from .models import Departamentos

# Create your views here.
 
def home(request):
 departamentos = Departamentos.objects.all()
 return render(request,"index.html", {"departamentos": departamentos})