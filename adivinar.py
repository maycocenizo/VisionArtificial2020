print("ingresa la cantidad de intentos para adivinar")
x = int(input())


def adivina(intentos):
    import random
    numero = random.randint(0, 100)
    for i in range(intentos):
        prueba = int(input("El numero es:"))
        if prueba == numero:
            print("adivinaste el numero, el numero es:{}" .format(prueba))
            break
        else:
            print("sigue intentando")
            print("el numero es real es:{}" .format(numero))

adivina(x)
