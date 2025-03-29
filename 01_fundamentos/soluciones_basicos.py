"""
Soluciones a los Ejercicios Básicos de Python 🐍
=============================================

Este archivo contiene las soluciones a los ejercicios propuestos en ejercicios_basicos.py
Úsalo solo después de haber intentado resolver los ejercicios por tu cuenta.
"""

# 🎯 Solución Ejercicio 1: Variables y Tipos de Datos
nombre = "Juan Pérez"
edad = 25
altura = 1.75
esta_estudiando = True

print("\n=== Información Personal ===")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura} metros")
print(f"¿Está estudiando?: {esta_estudiando}")


# 🎯 Solución Ejercicio 2: Operaciones Matemáticas
print("\n=== Calculadora Básica ===")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir por cero"

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


# 🎯 Solución Ejercicio 3: Strings
print("\n=== Manipulación de Strings ===")
nombre_completo = input("Ingresa tu nombre completo: ")

print(f"Mayúsculas: {nombre_completo.upper()}")
print(f"Minúsculas: {nombre_completo.lower()}")
print(f"Número de caracteres: {len(nombre_completo)}")
print(f"Primera letra: {nombre_completo[0]}")


# 🎯 Solución Ejercicio 4: Listas
frutas = ["manzana", "plátano", "naranja", "pera", "uva"]
print("\n=== Manipulación de Listas ===")
print(f"Lista original: {frutas}")

frutas.append("mango")
print(f"Después de agregar mango: {frutas}")

frutas.pop(1)  # Elimina el segundo elemento
print(f"Después de eliminar la segunda fruta: {frutas}")

print(f"Lista en orden inverso: {frutas[::-1]}")


# 🎯 Solución Ejercicio 5: Diccionarios
estudiante = {
    "nombre": "María García",
    "edad": 20,
    "calificaciones": [85, 90, 95]
}

promedio = sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"])
estudiante["promedio"] = promedio

print("\n=== Información del Estudiante ===")
for clave, valor in estudiante.items():
    print(f"{clave.capitalize()}: {valor}")


# 🎯 Solución Ejercicio 6: Condicionales
print("\n=== Clasificación por Edad ===")
edad = int(input("Ingresa tu edad: "))

if edad < 13:
    categoria = "Niño"
elif edad < 18:
    categoria = "Adolescente"
elif edad < 66:
    categoria = "Adulto"
else:
    categoria = "Adulto mayor"

print(f"Categoría: {categoria}")


# 🎯 Solución Ejercicio 7: Bucle For
print("\n=== Tabla de Multiplicar ===")
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


# 🎯 Solución Ejercicio 8: Bucle While
import random

print("\n=== Juego de Adivinar el Número ===")
numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

while not adivinado:
    intentos += 1
    numero_usuario = int(input("Adivina el número (1-100): "))
    
    if numero_usuario == numero_secreto:
        print(f"¡Correcto! Lo lograste en {intentos} intentos")
        adivinado = True
    elif numero_usuario < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")


# 🎯 Solución Ejercicio 9: Funciones
def analizar_numeros(lista_numeros):
    if not lista_numeros:
        return None
    
    return {
        "suma": sum(lista_numeros),
        "promedio": sum(lista_numeros) / len(lista_numeros),
        "maximo": max(lista_numeros),
        "minimo": min(lista_numeros)
    }

# Ejemplo de uso
numeros = [4, 2, 8, 6, 1, 9, 3, 5, 7]
resultado = analizar_numeros(numeros)
print("\n=== Análisis de Números ===")
for clave, valor in resultado.items():
    print(f"{clave.capitalize()}: {valor}")


# 🎯 Solución Ejercicio 10: Clases
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)
    
    def es_cuadrado(self):
        return self.ancho == self.alto
    
    def __str__(self):
        return f"Rectángulo de {self.ancho}x{self.alto}"

print("\n=== Rectángulos ===")
rectangulo1 = Rectangulo(5, 3)
rectangulo2 = Rectangulo(4, 4)

for i, rect in enumerate([rectangulo1, rectangulo2], 1):
    print(f"\nRectángulo {i}:")
    print(f"Dimensiones: {rect}")
    print(f"Área: {rect.area()}")
    print(f"Perímetro: {rect.perimetro()}")
    print(f"¿Es cuadrado?: {rect.es_cuadrado()}")

print("\n¡Felicidades! Has visto todas las soluciones. 🎉")
print("Recuerda que la práctica hace al maestro. ¡Sigue programando!") 