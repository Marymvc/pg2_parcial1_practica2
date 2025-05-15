from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Hola! Esta es la página principal de Películas.")