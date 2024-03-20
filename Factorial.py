#Calcular el factorial de un numero dado usando ciclo for.


#ej. Factorial: 5
#1x2x3x4x5 = 120

def calcular_factorial(numero):

 factorial = 1

 for i in range(1, numero + 1):

  factorial *= i

 return factorial



numero = int(input("Ingrese el número para calcular su factorial: "))

print("Factorial:", numero)

print("Resultado:", calcular_factorial(numero))