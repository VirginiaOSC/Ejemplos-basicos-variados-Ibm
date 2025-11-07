from math import pi

def area(r):
    #Función con la excepción TypeError y verificación de negativos
    if type(r) not in (float, int):
        #Verificamos los tipos correctos
        raise TypeError("El tipo de dato no es válido")
        #print("El tipo de dato no es válido")
    if r < 0:
       raise ValueError("El radio no puede ser negativo")
       #print("El radio no puede ser negativo")
    areaC = pi * (r**2)
    return areaC