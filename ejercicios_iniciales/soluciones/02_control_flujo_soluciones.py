"""
🔄 Soluciones: Estructuras de Control en Python 🔄
=============================================

Aquí encontrarás las soluciones a los ejercicios de control de flujo.
Recuerda: ¡Es importante intentar resolver los ejercicios por tu cuenta primero!
"""

# 🎯 Solución Ejercicio 1: Calificaciones
print("\n=== Solución: Calificaciones ===")
calificacion = float(input("Ingresa tu calificación (0-100): "))

if calificacion >= 60:
    print("¡Felicidades! Has aprobado")
    if calificacion >= 90:
        print("¡Excelente trabajo!")
    elif calificacion >= 80:
        print("¡Muy bien!")
    else:
        print("Sigue esforzándote")
else:
    print("Lo siento, has reprobado")
    print("Necesitas estudiar más")


# 🎯 Solución Ejercicio 2: Tabla de Multiplicar
print("\n=== Solución: Tabla de Multiplicar ===")
numero = int(input("¿Qué tabla de multiplicar quieres ver? "))

print(f"\nTabla del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


# 🎯 Solución Ejercicio 3: Adivina el Número
print("\n=== Solución: Adivina el Número ===")
import random

numero_secreto = random.randint(1, 10)
intentos = 0
adivinado = False

print("He pensado un número entre 1 y 10")
while not adivinado:
    intentos += 1
    intento = int(input("¿Qué número crees que es? "))
    
    if intento == numero_secreto:
        print(f"¡Correcto! Lo has adivinado en {intentos} intentos")
        adivinado = True
    elif intento < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")


# 🎯 Solución Ejercicio 4: Sumador de Números
print("\n=== Solución: Sumador de Números ===")
suma_positivos = 0
contador_negativos = 0

while True:
    numero = float(input("Ingresa un número (0 para terminar): "))
    
    if numero == 0:
        break
    elif numero > 0:
        suma_positivos += numero
    else:
        contador_negativos += 1

print(f"Suma de números positivos: {suma_positivos}")
print(f"Cantidad de números negativos: {contador_negativos}")


# 🌟 Solución Reto Extra: Calculadora con Menú
print("\n=== Solución: Calculadora con Menú ===")

while True:
    print("\nCalculadora Simple")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ")
    
    if opcion == "4":
        print("¡Gracias por usar la calculadora!")
        break
    
    if opcion in ["1", "2", "3"]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if opcion == "1":
            resultado = num1 + num2
            operacion = "suma"
        elif opcion == "2":
            resultado = num1 - num2
            operacion = "resta"
        else:
            resultado = num1 * num2
            operacion = "multiplicación"
        
        print(f"El resultado de la {operacion} es: {resultado}")
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4")

print("\n¡Felicidades! Estas son las soluciones a los ejercicios. 🎉")
print("Recuerda que puede haber diferentes formas de resolver cada ejercicio.")
print("Lo importante es que tu solución funcione correctamente.") 