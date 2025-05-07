#ejercicio 1

def ej1():
    i = 0
    a = 0
    while i < 5:
        x = int(input("Ingrese un número:"))
        if x > -1 and x % 2 == 0:
            a = a + x
        i = i + 1
    print("La suma de los enteros pares positivos es:", a)   
ej1()

#ejercicio 2


def ej2():
    edad = int(input("Ingrese su edad:"))
    if edad < 0:
        print("Error")
    if edad >= 0 and  edad < 13:
        print("Niño")
    if edad >= 13 and edad <= 17:
        print("Adolecente")
    if edad >= 18  and edad <= 59:
        print("Adulto")
    if edad >= 60:
        print("Adulto mayor")
        
ej2()

#ejercicio 3

def ej3():
    palabra = input("Ingrese su palabra:")
    l1 = "a"
    l2 = "e"
    l3 = "i"
    l4 = "o"
    l5 = "u"
    if l1 in palabra:
        a = palabra.count(l1)  
        print("a:", a)
    if l1 not in palabra:
        print("a:", 0)
    if l2 in palabra:
        e = palabra.count(l2)
        print("e:", e)
    if l2 not in palabra:
        print("e:", 0)
    if l3 in palabra:
        i = palabra.count(l3)
        print("i:", i)
    if l3 not in palabra:
        print("i:", 0)
    if l4 in palabra:
        o = palabra.count(l4)
        print("o:", o)
    if l4 not in palabra:
        print("o:", 0)
    if l5 in palabra:
        u = palabra.count(l5)
        print("u:", u)
    if l5 not in palabra:
        print("u:", 0)
    
ej3()
