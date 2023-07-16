from django.shortcuts import render,redirect
from .models import Estudiante
from .forms import EstudianteForm
from django.http import HttpRequest,HttpResponse

# Create your views here.
def home(request):
    estudiantes_registros = Estudiante.objects.all()
    contexto = {"estudiantes":estudiantes_registros}
    return render(request,"CORE/index.html",contexto)

def crear_estudiante(request: HttpRequest ) -> HttpResponse:
    
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("CORE:home")
    else:
        form = EstudianteForm()
    return render(request,"CORE/crear.html",{"form":form})