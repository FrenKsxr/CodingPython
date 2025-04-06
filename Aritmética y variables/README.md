# Guía de Aritmética y Variables en Python 🐍

## Tabla de Contenidos
1. [Imprimiendo](#imprimiendo)
2. [Aritmética](#aritmética)
3. [Comentarios](#comentarios)
4. [Variables](#variables)
   - [Creando variables](#creando-variables)
   - [Manipulando variables](#manipulando-variables)
   - [Usando múltiples variables](#usando-múltiples-variables)
   - [Depuración](#depuración)
5. [¿Qué sigue?](#qué-sigue)

## Imprimiendo
La función `print()` es una de las herramientas más básicas y útiles en Python. Te permite mostrar mensajes en la pantalla:

```python
print("¡Hola, mundo!")  # Muestra: ¡Hola, mundo!
print("Mi nombre es Python")  # Muestra: Mi nombre es Python
```

## Aritmética
Python es una excelente calculadora. Puedes realizar diferentes operaciones matemáticas:

| Operación | Símbolo | Ejemplo | Resultado |
|-----------|---------|---------|-----------|
| Suma | + | 5 + 3 | 8 |
| Resta | - | 10 - 4 | 6 |
| Multiplicación | * | 3 * 4 | 12 |
| División | / | 15 / 3 | 5 |
| Potencia | ** | 2 ** 3 | 8 |

```python
# Ejemplos de operaciones
print(1 + 2)   # Suma: 3
print(9 - 5)   # Resta: 4
print(4 * 3)   # Multiplicación: 12
print(10 / 2)  # División: 5.0
```

### Orden de Operaciones (PEMDAS)
1. **P**aréntesis
2. **E**xponentes
3. **M**ultiplicación y **D**ivisión
4. **A**dición y **S**ustracción

```python
print((2 + 3) * 4)  # Resultado: 20
print(2 + 3 * 4)    # Resultado: 14
```

## Comentarios
Los comentarios son notas que explican tu código. Se crean usando el símbolo #:

```python
# Esto es un comentario
print(2 + 3)  # Esta suma dará 5
```

## Variables
Las variables son como cajas donde guardamos información para usarla después.

### Creando variables
```python
edad = 25
nombre = "Ana"
altura = 1.75

print(edad)    # Muestra: 25
print(nombre)  # Muestra: Ana
print(altura)  # Muestra: 1.75
```

### Manipulando variables
Puedes cambiar el valor de una variable en cualquier momento:

```python
contador = 1
print(contador)  # Muestra: 1

contador = contador + 1
print(contador)  # Muestra: 2

contador = 10
print(contador)  # Muestra: 10
```

### Usando múltiples variables
Ejemplo práctico usando varias variables:

```python
# Calculando el área de un rectángulo
base = 5
altura = 3
area = base * altura
print(area)  # Muestra: 15

# Calculando tiempo en segundos
dias = 7
horas_por_dia = 24
minutos_por_hora = 60
segundos_por_minuto = 60

total_segundos = dias * horas_por_dia * minutos_por_hora * segundos_por_minuto
print(total_segundos)  # Muestra: 604800
```

### Depuración
Errores comunes y cómo solucionarlos:

```python
# ❌ Error: variable no definida
print(edadd)  # Error: name 'edadd' is not defined

# ✅ Correcto
edad = 25
print(edad)  # Funciona correctamente
```

## ¿Qué sigue?
Después de dominar estos conceptos básicos, podrás:
- Trabajar con estructuras de control (if, else)
- Aprender sobre bucles (for, while)
- Crear funciones
- Trabajar con listas y diccionarios

### 📝 Ejercicios Prácticos
1. Crea un programa que calcule tu edad en días
2. Escribe un programa que convierta euros a dólares
3. Calcula el perímetro y área de un círculo

### ⭐ Consejos
1. Usa nombres descriptivos para tus variables
2. Comenta tu código cuando sea necesario
3. Practica con ejemplos sencillos
4. No temas cometer errores, son parte del aprendizaje

¡Feliz programación! 🚀 