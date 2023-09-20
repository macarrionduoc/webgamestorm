from django.urls import path
from .views import index, registro, categoria, carro, categorias_accion, categorias_aventura, categorias_carreras, categorias_deportes, categorias_rol, categorias_shooters, categorias_terror, juego_apex, juego_show

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('registro', registro, name="registro"),
    path('categoria', categoria, name="categoria"),
    path('carro', carro, name="carro"),
    path('categorias/accion', categorias_accion, name="categorias_accion"),
    path('categorias/aventura', categorias_aventura, name="categorias_aventura"),
    path('categorias/carreras', categorias_carreras, name="categorias_carreras"),
    path('categorias/deportes', categorias_deportes, name="categorias_deportes"),
    path('categorias/rol', categorias_rol, name="categorias_rol"),
    path('categorias/shooters', categorias_shooters, name="categorias_shooters"),
    path('categorias/terror', categorias_terror, name="categorias_terror"),

    #path('juego/apex', juego_apex, name="juego_apex"),

    path('juego/<int:id>', juego_show, name="juego_show")

]