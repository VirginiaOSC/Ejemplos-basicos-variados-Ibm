from django.http import HttpResponse
import datetime

#Definición de la vista:
def saludo2(request):
   texto = """
   <html>
    <body>
    <h1>¡Hello World!</h1>
    </body>
    </html>"""
   return HttpResponse(texto)

#Definición de la vista para el contenido dinámico:
def fecha(request):
    miFecha = datetime.datetime.now()
    texto2 = """<html>
    "<body>
    <h2>Fecha y hora actuales: </h2>%s
    </body>
    </html>""" % miFecha
    return HttpResponse(texto2)


#Cálculo de la edad:
def calcEdad(request, year):
    edadActual = 33
    perido= year - 2025
    edadFutura=edadActual+perido
    documento="<html><body><h2>En el año %s tendrás %s años.</h2></body></html>"%(year, edadFutura)
    return HttpResponse(documento)