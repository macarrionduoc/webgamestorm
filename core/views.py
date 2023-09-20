from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro.html')

def categoria(request):
    return render(request, 'categoria.html')

def carro(request):
    return render(request, 'carro.html')

def categorias_accion(request):
    return render(request, 'categorias/accion.html')

def categorias_aventura(request):
    return render(request, 'categorias/aventura.html')

def categorias_carreras(request):
    return render(request, 'categorias/carreras.html')

def categorias_deportes(request):
    return render(request, 'categorias/deportes.html')

def categorias_rol(request):
    return render(request, 'categorias/rol.html')

def categorias_shooters(request):
    return render(request, 'categorias/shooters.html')

def categorias_terror(request):
    return render(request, 'categorias/terror.html')

