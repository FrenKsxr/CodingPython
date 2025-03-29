"""
🎯 Primer Programa en Python
==========================

Este es un ejemplo que muestra diferentes formas de usar print
y recibir input del usuario.

Autor: Tu Nombre
Fecha: 2024
"""

# 1. Mensaje simple
print("¡Hola! Este es mi primer programa en Python")

# 2. Múltiples mensajes
print("Python")
print("es")
print("divertido")

# 3. Usando separadores
print("Python", "es", "divertido", sep=" 🐍 ")

# 4. Input básico
nombre = input("¿Cómo te llamas? ")
print("¡Hola,", nombre + "!")

# 5. Usando formato de strings (f-strings)
edad = input("¿Cuántos años tienes? ")
print(f"¡Wow! {nombre} tiene {edad} años")

# 6. Líneas decorativas
print("=" * 30)
print("Programa finalizado")
print("=" * 30)

# 7. Arte ASCII simple
print("""
    /\\___/\\
   (  o o  )
   (  =^=  ) 
    (______)
""")

# 8. Mensaje de despedida
input("\nPresiona Enter para salir...") 