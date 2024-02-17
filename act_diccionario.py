#realizar un programa para el manejo de un diccionario
#con el siguinte menu
#1-agregar elemento
#2-modificar elemento
#3-borrar elemento
#4-salir

dic = {}

while True:
    print("Menu de lista")
    print("1. Agregar elemento")
    print("2. modificar elemento")
    print("3. borrar elemento")
    print("4. Salir")

    opcion = input("seleccione una opcion: ")

    if opcion == "1":

        elemento = input("Ingrese un elemento al diccionario:  ")
        dic[elemento] = ""
        significado =  input("Ingresa el significado: ")
        dic[elemento] = significado

        print(dic)

    elif opcion == "2":

        print(dic)

        modi = input("Que elemento desea modificar: ")
        dic[modi]=""
        dic.pop(modi)
        NuevoElemento = input("Ingrese nuevo elemento")
        dic[NuevoElemento] = ""
        significadoN = input("Ingresa el significado: ")
        dic[NuevoElemento] = significadoN

        print(dic)


    elif opcion == "3":
        input(dic)
        borra = input("ingresa el elemento que deseas borrar: ")
        dic.pop(borra)


    elif opcion == "4":
        print("Saliendo del programa ¡ADIOS!")
        break

    else:
        print("opcion no valida")


