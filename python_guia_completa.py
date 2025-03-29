"""
# ======= GUÍA COMPLETA DE PYTHON =======
# Este archivo contiene ejemplos y explicaciones de los conceptos más importantes en Python

# 1. VARIABLES Y TIPOS DE DATOS BÁSICOS
nombre = "Juan"  # String (cadena de texto)
edad = 25        # Integer (número entero)
altura = 1.75    # Float (número decimal)
es_estudiante = True  # Boolean (verdadero/falso)

print("\n=== Variables y Tipos de Datos ===")
print(f"Nombre: {nombre} - Tipo: {type(nombre)}")
print(f"Edad: {edad} - Tipo: {type(edad)}")
print(f"Altura: {altura} - Tipo: {type(altura)}")
print(f"¿Es estudiante?: {es_estudiante} - Tipo: {type(es_estudiante)}")

# 2. ESTRUCTURAS DE DATOS
# Listas (mutables, ordenadas)
frutas = ["manzana", "banana", "naranja"]
print("\n=== Listas ===")
print(f"Lista original: {frutas}")
frutas.append("pera")  # Agregar elemento
print(f"Después de append: {frutas}")
print(f"Primer elemento: {frutas[0]}")

# Tuplas (inmutables, ordenadas)
coordenadas = (10, 20)
print("\n=== Tuplas ===")
print(f"Coordenadas: {coordenadas}")
print(f"Coordenada X: {coordenadas[0]}")

# Diccionarios (pares clave-valor)
persona = {
    "nombre": "María",
    "edad": 30,
    "ciudad": "Madrid"
}
print("\n=== Diccionarios ===")
print(f"Persona: {persona}")
print(f"Nombre: {persona['nombre']}")

# 3. ESTRUCTURAS DE CONTROL
# If-elif-else
print("\n=== Condicionales ===")
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")

# Bucles
print("\n=== Bucles ===")
# For
print("Bucle for:")
for i in range(3):
    print(f"Iteración {i}")

# While
print("\nBucle while:")
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

# 4. FUNCIONES
print("\n=== Funciones ===")
def saludar(nombre, edad=None):
    if edad:
        return f"¡Hola {nombre}! Tienes {edad} años."
    return f"¡Hola {nombre}!"

print(saludar("Ana"))
print(saludar("Pedro", 25))

# 5. CLASES Y OBJETOS (POO)
print("\n=== Programación Orientada a Objetos ===")
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"Me llamo {self.nombre} y tengo {self.edad} años"

persona1 = Persona("Carlos", 28)
print(persona1.presentarse())

# 6. MANEJO DE ERRORES
print("\n=== Manejo de Errores ===")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero")
finally:
    print("Este bloque siempre se ejecuta")

# 7. TRABAJANDO CON ARCHIVOS
print("\n=== Manejo de Archivos ===")
# Escribir en un archivo
with open("ejemplo.txt", "w") as archivo:
    archivo.write("¡Hola desde Python!")

# Leer el archivo
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print(f"Contenido del archivo: {contenido}")

# 8. COMPRENSIÓN DE LISTAS
print("\n=== Comprensión de Listas ===")
numeros = [1, 2, 3, 4, 5]
cuadrados = [n**2 for n in numeros]
print(f"Números originales: {numeros}")
print(f"Números al cuadrado: {cuadrados}")

# 9. FUNCIONES LAMBDA
print("\n=== Funciones Lambda ===")
multiplicar = lambda x, y: x * y
print(f"2 x 3 = {multiplicar(2, 3)}")

# 10. MÓDULOS Y PAQUETES
print("\n=== Módulos ===")
import math
print(f"Valor de PI: {math.pi}")
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")

if __name__ == "__main__":
    print("\n¡Gracias por aprender Python! 🐍")
""" 