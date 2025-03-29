"""
🔄 Estructuras de Control en Python 🔄
===================================

En este módulo aprenderemos a controlar el flujo de nuestros programas
usando if, for y while.

📝 Instrucciones:
1. Completa cada ejercicio paso a paso
2. Ejecuta el código y observa los resultados
3. Modifica los ejemplos para experimentar
"""

# 🎯 Ejercicio 1: Decisiones Simples (if)
# Objetivo: Aprender a tomar decisiones en el código
print("\n=== Ejercicio 1: Decisiones ===")

edad = int(input("¿Cuál es tu edad? "))

if edad < 13:
    print("Eres un niño")
elif edad < 20:
    print("Eres un adolescente")
elif edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")

# Tu turno: Crea un programa que:
# 1. Pida al usuario su calificación (0-100)
# 2. Muestre si aprobó o no (se aprueba con 60 o más)
print("\n--- Tu Turno: Calificaciones ---")
# Tu código aquí:



# 🎯 Ejercicio 2: Bucles For
# Objetivo: Aprender a repetir acciones
print("\n=== Ejercicio 2: Bucle For ===")

# Ejemplo: Contar del 1 al 5
print("Contando del 1 al 5:")
for numero in range(1, 6):
    print(numero)

# Ejemplo: Recorrer una lista
frutas = ["manzana", "banana", "naranja", "pera"]
print("\nLista de frutas:")
for fruta in frutas:
    print("- " + fruta)

# Tu turno: Crea un programa que:
# 1. Muestre la tabla de multiplicar del número que elija el usuario
print("\n--- Tu Turno: Tabla de Multiplicar ---")
# Tu código aquí:



# 🎯 Ejercicio 3: Bucles While
# Objetivo: Repetir acciones mientras una condición sea verdadera
print("\n=== Ejercicio 3: Bucle While ===")

# Ejemplo: Cuenta regresiva
print("Cuenta regresiva:")
contador = 5
while contador > 0:
    print(contador)
    contador -= 1
print("¡Despegue! 🚀")

# Tu turno: Crea un juego simple donde:
# 1. El programa elija un número aleatorio entre 1 y 10
# 2. El usuario debe adivinarlo
# 3. El programa debe dar pistas (mayor/menor)
print("\n--- Tu Turno: Adivina el Número ---")
import random
numero_secreto = random.randint(1, 10)
# Tu código aquí:



# 🎯 Ejercicio 4: Combinando Todo
# Objetivo: Usar if, for y while juntos
print("\n=== Ejercicio 4: Ejercicio Combinado ===")

# Ejemplo: Encontrar números pares
print("Números pares del 1 al 10:")
for num in range(1, 11):
    if num % 2 == 0:
        print(num, "es par")
    else:
        print(num, "es impar")

# Tu turno: Crea un programa que:
# 1. Pida números al usuario hasta que ingrese 0
# 2. Muestre la suma de los números positivos ingresados
# 3. Muestre la cantidad de números negativos ingresados
print("\n--- Tu Turno: Sumador de Números ---")
# Tu código aquí:



# 🌟 Reto Extra 🌟
# Crea un pequeño menú que:
# 1. Muestre opciones (1: Sumar, 2: Restar, 3: Multiplicar, 4: Salir)
# 2. Pida dos números y realice la operación seleccionada
# 3. Se repita hasta que el usuario elija salir

print("\n=== Reto Extra: Calculadora con Menú ===")
# Tu código aquí:



# 💡 Experimentos Sugeridos:
# 1. Modifica los rangos en los bucles for
# 2. Cambia las condiciones en los if
# 3. Crea diferentes tipos de menús
# 4. Combina diferentes estructuras de control

print("\n¡Felicidades! Has completado los ejercicios de control de flujo. 🎉")
print("Recuerda: La práctica hace al maestro. ¡Sigue experimentando!") 