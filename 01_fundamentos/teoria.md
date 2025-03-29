# 📘 Fundamentos de Python

## 🌟 Introducción
Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Es conocido por su simplicidad y legibilidad.

## 📌 Contenido

### 1. Variables y Tipos de Datos
```python
# Strings (cadenas de texto)
nombre = "Ana"
apellido = 'García'

# Números
edad = 25          # Integer (entero)
altura = 1.75      # Float (decimal)
complejo = 3 + 4j  # Número complejo

# Booleanos
es_estudiante = True
tiene_mascota = False
```

### 2. Operadores
```python
# Aritméticos
suma = 5 + 3
resta = 10 - 4
multiplicacion = 6 * 2
division = 15 / 3
potencia = 2 ** 3
modulo = 17 % 5

# Comparación
igual_que = 5 == 5
mayor_que = 7 > 3
menor_igual = 4 <= 4
```

### 3. Estructuras de Datos

#### 3.1 Listas
```python
frutas = ["manzana", "banana", "naranja"]
numeros = [1, 2, 3, 4, 5]

# Operaciones comunes
frutas.append("pera")        # Agregar elemento
frutas.remove("banana")      # Eliminar elemento
primer_elemento = frutas[0]  # Acceder a elemento
```

#### 3.2 Tuplas
```python
# Inmutables después de crearse
coordenadas = (10, 20)
fecha = (25, "Diciembre", 2023)
```

#### 3.3 Diccionarios
```python
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a valores
nombre = persona["nombre"]
edad = persona.get("edad")
```

### 4. Estructuras de Control

#### 4.1 Condicionales
```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
```

#### 4.2 Bucles
```python
# For
for i in range(5):
    print(i)

# While
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### 5. Funciones
```python
def saludar(nombre):
    return f"¡Hola, {nombre}!"

def suma(a, b=0):
    return a + b

# Función con múltiples parámetros
def info_persona(nombre, edad, ciudad="Desconocida"):
    return f"{nombre} tiene {edad} años y vive en {ciudad}"
```

### 6. Programación Orientada a Objetos
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"Me llamo {self.nombre} y tengo {self.edad} años"
```

## 🎯 Consejos de Estilo

1. **Indentación**: Usa 4 espacios (no tabuladores)
2. **Nombres**:
   - variables_y_funciones: minúsculas con guiones bajos
   - ClasesEnPascalCase: primera letra mayúscula
3. **Comentarios**: Usa comentarios para explicar el "por qué", no el "qué"

## 🚫 Errores Comunes a Evitar

1. Olvidar los dos puntos `:` en if, for, while, etc.
2. Confundir `=` (asignación) con `==` (comparación)
3. No mantener una indentación consistente
4. Usar variables antes de definirlas

## 📚 Recursos Adicionales

1. [Documentación oficial de Python](https://docs.python.org/es/)
2. [Python Tutorial - W3Schools](https://www.w3schools.com/python/)
3. [Real Python](https://realpython.com/)

## 🔍 Próximos Pasos

1. Revisa los ejercicios en `ejercicios_basicos.py`
2. Intenta resolverlos sin mirar las soluciones
3. Compara tus respuestas con `soluciones_basicos.py`
4. Practica creando tus propios programas pequeños 