from django.http import HttpResponse
import datetime

def saludo(request):    
    return HttpResponse("<html><body><h1>¡Hola, mundo! Esta es mi primera vista en Django.</h1></body></html>")

