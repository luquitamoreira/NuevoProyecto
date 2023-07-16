from django.shortcuts import render
from .models import Estudiante
# Create your views here.
def home(request):
    estudiantes_registros=Estudiante.objects.all()
    contexto = {"estudiantes":estudiantes_registros}
    return render(request,"CORE/index.html",contexto)