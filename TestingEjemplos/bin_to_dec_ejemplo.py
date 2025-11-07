def decimal(binary_str):
    """ Convierte cadenas binarias a sus equivalentes decimales.
Lanzar ValueError si binary_str contiene caracteres distintos de 0 y 1"""
    remove_0_and_1 = binary_str.replace('0', '').replace('1', '')
    if len(remove_0_and_1) > 0:
        raise ValueError("La cadena contiene caracteres distintos de 0 y 1")
    decimal_value = 0
    place = 1 #Posición
    dec = 0 #El valor decimal

    for bit in binary_str[::-1]: #Recorremos la cadena al revés
        if bit == '1':
            dec += place #Sumamos el valor de la posición actual para acumular la suma decimal que depende de las potencias en base 2 de derecha a izuquirda.
        place *= 2  #Multiplicamos la posición por 2 (base binaria, potencias de 2)
    return dec

