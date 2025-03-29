"""
🐍 Primeros Pasos en Python 🐍
============================

¡Bienvenido a tu primera experiencia con Python! 
Este archivo contiene ejercicios muy básicos para empezar a programar.

📝 Instrucciones:
1. Lee cada ejercicio cuidadosamente
2. Intenta resolverlo por tu cuenta
3. Si te atascas, mira las pistas
4. ¡No tengas miedo de experimentar!
"""

# 🎯 Ejercicio 1: Tu primer programa
# Objetivo: Mostrar un mensaje en pantalla
# Pista: Usa la función print()

print("¡Hola, mundo!")  # ¡Prueba a cambiar el mensaje!


# 🎯 Ejercicio 2: Variables simples
# Objetivo: Crear y mostrar variables
# Pista: Puedes usar diferentes tipos de datos

# Tu turno: Crea variables con tu información
nombre = "Ana"  # Cambia por tu nombre
edad = 25       # Cambia por tu edad
altura = 1.65   # Cambia por tu altura

# Mostramos la información
print("\n=== Tu Información ===")
print("Nombre:", nombre)
print("Edad:", edad, "años")
print("Altura:", altura, "metros")


# 🎯 Ejercicio 3: Operaciones básicas
# Objetivo: Realizar cálculos simples
# Pista: Prueba diferentes operadores: +, -, *, /

# Ejemplo: Calculadora simple
numero1 = 10
numero2 = 5

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("\n=== Operaciones Básicas ===")
print(numero1, "+", numero2, "=", suma)
print(numero1, "-", numero2, "=", resta)
print(numero1, "×", numero2, "=", multiplicacion)
print(numero1, "÷", numero2, "=", division)


# 🎯 Ejercicio 4: Input del usuario
# Objetivo: Recibir datos del usuario
# Pista: Usa la función input()

print("\n=== Interacción con Usuario ===")
tu_nombre = input("¿Cómo te llamas? ")
print("¡Hola,", tu_nombre + "!")

# Tu turno: Pide la edad al usuario y muestra cuántos años tendrá en 10 años
tu_edad = int(input("¿Cuántos años tienes? "))
edad_futura = tu_edad + 10
print("En 10 años tendrás", edad_futura, "años")


# 🎯 Ejercicio 5: Strings divertidos
# Objetivo: Manipular textos
# Pista: Los strings tienen muchos métodos útiles

mensaje = "python es divertido"
print("\n=== Jugando con Texto ===")
print("Original:", mensaje)
print("En mayúsculas:", mensaje.upper())
print("En minúsculas:", mensaje.lower())
print("Capitalizado:", mensaje.capitalize())
print("Número de caracteres:", len(mensaje))


# 🌟 Reto Extra 🌟
# ¿Puedes crear un programa que:
# 1. Pida el nombre del usuario
# 2. Pida su año de nacimiento
# 3. Calcule su edad aproximada
# 4. Muestre un mensaje personalizado con toda la información?

print("\n=== Reto Extra ===")
# Tu código aquí:



# 💡 Experimentos Sugeridos:
# 1. Cambia los mensajes de print
# 2. Crea nuevas variables con otros tipos de datos
# 3. Prueba diferentes operaciones matemáticas
# 4. Juega con otros métodos de strings (busca en la documentación)

print("\n¡Felicidades! Has completado los ejercicios básicos. 🎉")
print("Intenta modificar el código y experimenta con nuevas ideas.") 