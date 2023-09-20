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


def juego_apex(request):
    contexto = {
        'nombre' : 'APEX'
    }
    return render(request, 'juego/apex.html', contexto)

def juego_show(request, id):
    juegos = ['apex', 'battlegrounds', 'destiny2', 'warframe', 'gta5', 'naraka', 'rust', 'wayfinder', 'automobilista2', 'forza', 'need_for_speed', 'need_for_speed_delux', 'thecrew2', 'f1_23', 'fc24', 'fifa_23', 'madden_24', 'nba_24', 'black_desert', 'elden_ring', 'final_fantasy_xiv', 'lostark', 'couter_strike', 'metro', 'rainbowsix', 'team_fortress_2', 'the_texas_chain_saw_massacre', 'dead_daylight', 'dying_light', 'remnant', 'the_outlast_trials']
    imagenes = ['img/accion_apex.jpg', 'img/accion_battlegrounds.jpg', 'img/accion_destiny_2.jpg', 'img/accion_warframe.jpg', 'img/aventura_gta_5.jpg', 'img/aventura_naraka.jpg', 'img/aventura_rust.jpg', 'img/aventura_wayfinder.jpg', 'img/carreras_automobilista_2.jpg', 'img/carreras_forza.jpg', 'img/carreras_needForSpeed.jpg', 'img/carreras_needForSpeed_Delux.jpg', 'img/carreras_theCrew_2.jpg', 'img/deportes_f1_23.jpg', 'img/deportes_fc24.jpg', 'img/deportes_fifa_23.jpg', 'img/deportes_madden_24.jpg', 'img/deportes_nba_24.jpg', 'img/rol_blackDesert.jpg', 'img/rol_eldenRing.jpg', 'img/rol_finalFantasy_xiv.jpg', 'img/rol_lostark.jpg', 'img/shooter_couterStrike.jpg', 'img/Shooter_metro.jpg', 'img/shooter_rainbowsix.jpg', 'img/shooter_teamFortress_2.jpg', 'img/teeror_theTexasChainSawMassacre.jpg', 'img/terror_deadDaylight.jpg', 'img/terror_dyingLight.jpg', 'img/terror_remnant.jpg', 'img/terror_theOutlastTrials.jpg']
    
    juego = juegos[id-1]
    img = imagenes[id-1]

    contexto = {
        'nombre' : juego,
        'img'   : img
    }
    return render(request, 'juego/show.html', contexto)
