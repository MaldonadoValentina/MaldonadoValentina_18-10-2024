from django.shortcuts import render
from .models import AlumnoT

# Create your views here.
def index_vista(request):
    objeto=AlumnoT.objects.all().order_by("id") # nuevo + el diccionario
    return render(request,"index.html",{"Objeto:":objeto})
