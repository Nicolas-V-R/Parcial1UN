#ejercicio 1

def ej1():
    i = 0 # Defino mi contador
    a = 0 # Defino variable
    while i < 5: # Pongo un condicional para bucle
        x = int(input("Ingrese un número:")) # Pido al usuario ingresar los numeros
        if x > -1 and x % 2 == 0: # Coloco los condicionales para que se sume
            a = a + x # Sumo el numero que ingresado si cumple las condiciones
        i = i + 1 # e sumo uno a mi variable de contador
    print("La suma de los enteros pares positivos es:", a) #Imprimo el resultado
ej1()

#ejercicio 2


def ej2():
    edad = int(input("Ingrese su edad:")) # Pido al usuario ingresar la edad
    if edad < 0: # Coloco los condicional para imprimir un mensaje
        print("Error") #Imprimo el mensaje
    if edad >= 0 and  edad < 13: # Coloco los condicionales para imprimir un mensaje
        print("Niño") #Imprimo el mensaje
    if edad >= 13 and edad <= 17:  # Coloco los condicionales para imprimir un mensaje
        print("Adolecente") #Imprimo el mensaje
    if edad >= 18  and edad <= 59:  # Coloco los condicionales para imprimir un mensaje
        print("Adulto") #Imprimo el mensaje
    if edad >= 60:  # Coloco los condicional para imprimir un mensaje
        print("Adulto mayor") #Imprimo el mensaje
        
ej2()

#ejercicio 3

def ej3():
    palabra = input("Ingrese su palabra:") # Pido al usuario ingresar la palabra
    l1 = "a" # Defino las letras 
    l2 = "e"
    l3 = "i"
    l4 = "o"
    l5 = "u"
    if l1 in palabra: # Coloco los condicionales para contar en la palabra
        a = palabra.count(l1)  # Cuento la letra en la palabra
        print("a:", a)
    if l1 not in palabra:
        print("a:", 0)
    if l2 in palabra: # Coloco los condicionales para contar en la palabra
        e = palabra.count(l2) # Cuento la letra en la palabra
        print("e:", e)
    if l2 not in palabra:
        print("e:", 0)
    if l3 in palabra: # Coloco los condicionales para contar en la palabra
        i = palabra.count(l3) # Cuento la letra en la palabra
        print("i:", i)
    if l3 not in palabra:
        print("i:", 0)
    if l4 in palabra: # Coloco los condicionales para contar en la palabra
        o = palabra.count(l4) # Cuento la letra en la palabra
        print("o:", o)
    if l4 not in palabra:
        print("o:", 0)
    if l5 in palabra: # Coloco los condicionales para contar en la palabra
        u = palabra.count(l5) # Cuento la letra en la palabra
        print("u:", u)
    if l5 not in palabra:
        print("u:", 0)
    
ej3()
