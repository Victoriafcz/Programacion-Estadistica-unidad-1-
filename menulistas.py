Primerlista=[]


class Primerlsita:
    pass


class Primeralista:
    pass


while True:
    print("Menu de lista")
    print("1. Agregar elemento")
    print("2. Borrar elemento")
    print("3. Iprimir lista")
    print("4. Salir")

    opcion=input("seleccione una opcion")
    if opcion == "1":
        elemento = input("Ingrese elemento")
        Primeralista.append(elemento)

    elif opcion == "2" :
        print(Primerlsita)
        indice = int(input("ingrese el indice que desea borrar: "))
        Primeralista.pop(indice)
        print("Elemento borrado correctaamente")


    elif opcion == "3" :
        print("Lista Actual")
        print(Primeralista)

    elif opcion == "4":
        print("saliendo del programa")
        break

    else:
        print("opcion no valida")
