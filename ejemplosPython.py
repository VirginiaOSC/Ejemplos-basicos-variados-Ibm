import random

print('¡Hola mundo!')

lista = [1, 2, 3, 4, 5]
random.choice(lista)
print(random.choice(lista))


def log_ejemplo(*args):
    mensaje = input("Ingrese un mensaje para el log: ")
    print(type(mensaje))
    print(f"{args}")
          
log_ejemplo()
log_ejemplo(1, 2, 3)


num = 3
texto = "3"

print(num == texto)


l = list()
texto = input("Escriba un número: ")
if texto.isnumeric():
    num = int(texto)
    l.append(num)
    print(f"Se añadió el número: {num} a la lista: {l}")
else:
    print("EL número no es entero.")

d ={'11111111': 20, '22222222': 30}
texto = input("Escriba su DNI: ")
if texto in d:
    edad = str(d[texto])
    print(f"La edad asociada al DNI {texto} es {edad}")
else:
    edad = input("Indroduzca la edad para asociarla a su DNI:")
    if edad.isnumeric():
        num = int(edad)
        d[texto] = num
        print(f"Se añadió la edad: {num} al DNI: {texto}")



edad = int(input("Ingrese su edad: "))
while edad < 0:
    print("Edad no válida. Intente de nuevo.")
    edad = int(input("Ingrese su edad: "))
print(f"Su edad es {edad} años.")
print("Tu edad es: ", edad)
print("tu edad es: " + str(edad))
