#Realizar un programa que realice los siguientes funciones con un menu
#1. Conversor de centigrados o Fohrenheit
#2. Funcion que diga si un numero es positivo o negativo
#3. Funcion que diga si un numero es par o impar
#4. Funcion que reciba un numero del 1 al 10 y lo convierta en letra
#5. Funcion que reciba una lista de 5 numeros y devuelva la sumatoria
#6. Salir

def convertir_centigrados_a_fahrenheit():
    centigrados = float(input("Ingresa la temperatura en grados centígrados: "))
    fahrenheit = (centigrados * 9 / 5) + 32
    print("La temperatura en grados Fahrenheit es:", fahrenheit)


def Positivo_o_negativo():
    numero = float(input("Ingresa un número: "))
    if numero > 0:
        print("El número es positivo.")
    else:

        print("El número es negativo.")


def Par_o_impar():
    numero = int(input("Ingresa un número entero: "))
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")


def convertir_numero_a_letra():
    numeros_letras = {1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco', 6: 'seis', 7: 'siete', 8: 'ocho',
                      9: 'nueve', 10: 'diez'}
    numero = int(input("Ingresa un número del 1 al 10: "))
    if numero in numeros_letras:
        print("El número en letra es:", numeros_letras[numero])
    else:
        print("Mayor a 10.")


def calcular_sumatoria():
    numeros = [float(input(f"Ingresa el número {i + 1}: ")) for i in range(5)]
    suma = sum(numeros)
    print("La suma de los números es:", suma)


while True:
    print("\n--- MENÚ ---")
    print("1. Conversor de Centigrados a Fahrenheit")
    print("2. Verificar si un número es positivo o negativo")
    print("3. Verificar si un número es par o impar")
    print("4. Conversor de número del 1 al 10 a letra")
    print("5. Sumatoria de una lista de 5 números")
    print("6. Salir")
    opcion = input("Selecciona una opción (1-6): ")

    if opcion == '1':
        convertir_centigrados_a_fahrenheit()
    elif opcion == '2':
        Positivo_o_negativo()
    elif opcion == '3':
        Par_o_impar()
    elif opcion == '4':
        convertir_numero_a_letra()
    elif opcion == '5':
        calcular_sumatoria()
    elif opcion == '6':
        print("¡HASTA PRONTO!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")











