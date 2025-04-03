# 📚 Aritmética y Variables en Python

## 🎯 Introducción

¡Bienvenido a tu primer día de programación! Este curso está diseñado para personas que nunca han escrito una línea de código y están interesadas en aprender ciencia de datos y aprendizaje automático. Si ya tienes experiencia en programación y solo quieres aprender Python, puedes saltar directamente al curso de Python.

## 🚀 ¿Qué Aprenderás?

En este curso aprenderás a:
- Usar código para que una computadora realice tareas específicas
- Trabajar con Python, uno de los lenguajes más populares para ciencia de datos
- Prepararte para cursos avanzados de Python y Machine Learning

## 💻 Imprimiendo Mensajes

Una de las tareas más simples (¡y más importantes!) que puedes pedirle a una computadora es imprimir un mensaje.

En Python, usamos la función `print()` para mostrar mensajes. El mensaje va entre paréntesis y comillas:

```python
print("¡Hola, mundo!")
# Salida: ¡Hola, mundo!
```

## ➗ Operaciones Aritméticas

Python puede realizar cálculos matemáticos. Aquí tienes algunos ejemplos:

```python
# Suma
print(1 + 2)  # Salida: 3

# Resta
print(9 - 5)  # Salida: 4
```

### 📊 Tabla de Operaciones

| Operación    | Símbolo | Ejemplo    | Resultado |
|--------------|---------|------------|-----------|
| Suma         | +       | 1 + 2      | 3         |
| Resta        | -       | 5 - 4      | 1         |
| Multiplicación| *      | 2 * 4      | 8         |
| División     | /       | 6 / 3      | 2         |
| Potencia     | **      | 3 ** 2     | 9         |

### 🔢 Orden de Operaciones

Python sigue la regla PEMDAS:
- Paréntesis
- Exponentes
- Multiplicación/División
- Adición/Sustracción

```python
print(((1 + 3) * (9 - 2) / 2) ** 2)  # Salida: 196.0
```

## 💭 Comentarios

Los comentarios son notas que explican el código. Comienzan con `#`:

```python
# Multiplicar 3 por 2
print(3 * 2)  # Salida: 6
```

## 📝 Variables

Las variables son como contenedores que almacenan valores para usarlos más tarde.

### Creando Variables

```python
# Crear una variable y asignarle un valor
test_var = 4 + 5
print(test_var)  # Salida: 9
```

### 📋 Reglas para Nombres de Variables

1. No pueden tener espacios
2. Solo pueden incluir letras, números y guiones bajos
3. Deben comenzar con una letra o guión bajo
4. Son sensibles a mayúsculas y minúsculas

### 🔄 Manipulando Variables

```python
# Crear y cambiar el valor de una variable
mi_var = 3
print(mi_var)  # Salida: 3

mi_var = 100
print(mi_var)  # Salida: 100

# Incrementar el valor
mi_var = mi_var + 3
print(mi_var)  # Salida: 103
```

### 📊 Usando Múltiples Variables

```python
# Calcular segundos en 4 años
num_years = 4
dias_por_año = 365
horas_por_dia = 24
mins_por_hora = 60
segs_por_min = 60

total_segs = segs_por_min * mins_por_hora * horas_por_dia * dias_por_año * num_years
print(total_segs)  # Salida: 126144000
```

## 🐛 Depuración

Errores comunes al trabajar con variables:

```python
# Error: nombre de variable mal escrito
print(horas_por_dy)  # NameError: name 'horas_por_dy' is not defined

# Corrección
print(horas_por_dia)  # Salida: 24
```

## 📚 Ejercicios Prácticos

1. Crea una variable con tu edad y otra con tu año de nacimiento
2. Calcula el área de un rectángulo usando variables
3. Convierte grados Celsius a Fahrenheit usando variables

## 🎯 Recursos Adicionales

- [Documentación de Python sobre Variables](https://docs.python.org/es/3/tutorial/introduction.html#first-steps-towards-programming)
- [Tutorial de Operadores Aritméticos](https://docs.python.org/es/3/tutorial/introduction.html#using-python-as-a-calculator)
- [Guía de Estilo PEP 8](https://www.python.org/dev/peps/pep-0008/)

---

¡Feliz programación! 🚀 