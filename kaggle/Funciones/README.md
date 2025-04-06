# Guía Completa de Funciones en Python 🐍

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Introducción a funciones: un ejemplo simple](#introducción-a-funciones-un-ejemplo-simple)
   - [Encabezado](#encabezado)
   - [Cuerpo](#cuerpo)
3. [Cómo ejecutar (o "llamar") una función](#cómo-ejecutar-una-función)
4. [Nombrando funciones](#nombrando-funciones)
5. [Un ejemplo más complejo](#un-ejemplo-más-complejo)
6. [Alcance de variables](#alcance-de-variables)
7. [Funciones con múltiples argumentos](#funciones-con-múltiples-argumentos)
8. [Funciones sin argumentos](#funciones-sin-argumentos)

## Introducción
Las funciones son bloques de código diseñados para realizar una tarea específica. Son fundamentales en la programación ya que nos permiten:
- Organizar mejor nuestro código
- Reutilizar código sin necesidad de duplicarlo
- Hacer nuestros programas más eficientes y mantenibles

## Introducción a funciones: un ejemplo simple
Veamos un ejemplo básico de una función que suma 3 a cualquier número:

```python
def add_three(input_var):
    output_var = input_var + 3
    return output_var
```

### Encabezado
El encabezado de una función contiene:
- La palabra clave `def` que indica que vamos a definir una función
- El nombre de la función (en este caso `add_three`)
- Los parámetros entre paréntesis (en este caso `input_var`)
- Dos puntos `:` al final

### Cuerpo
El cuerpo de la función incluye:
- Código indentado (4 espacios)
- Las operaciones que realizará la función
- Generalmente un `return` para devolver el resultado

## Cómo ejecutar una función
Para usar una función, la "llamamos" con sus argumentos:
```python
nuevo_numero = add_three(10)  # Resultado: 13
```

## Nombrando funciones
Reglas para nombrar funciones:
- Usar solo letras minúsculas
- Separar palabras con guiones bajos
- El nombre debe ser descriptivo
Ejemplo: `calcular_total`, `obtener_usuario`, `validar_datos`

## Un ejemplo más complejo
Ejemplo práctico de una función para calcular el salario:
```python
def calcular_pago(horas_trabajadas):
    pago_bruto = horas_trabajadas * 15
    pago_neto = pago_bruto * (1 - 0.12)  # 12% de impuestos
    return pago_neto
```

## Alcance de variables
- Variables dentro de la función (locales): solo accesibles dentro de la función
- Variables fuera de la función (globales): accesibles en todo el código
- Las variables locales se destruyen cuando la función termina

## Funciones con múltiples argumentos
Podemos crear funciones que acepten varios parámetros:
```python
def calcular_pago_detallado(horas, tarifa_hora, impuestos):
    pago_bruto = horas * tarifa_hora
    pago_neto = pago_bruto * (1 - impuestos)
    return pago_neto
```

## Funciones sin argumentos
También existen funciones que no requieren parámetros:
```python
def saludar():
    print("¡Hola, bienvenido!")
```

---
### 📝 Nota importante
Las funciones son una herramienta fundamental en la programación que nos ayudan a:
- Evitar la repetición de código
- Hacer el código más legible
- Facilitar el mantenimiento
- Organizar mejor nuestro programa

### 🔍 Ejemplos prácticos
```python
# Calculando el pago para diferentes casos
pago_tiempo_completo = calcular_pago(40)  # 40 horas -> $528.00
pago_medio_tiempo = calcular_pago(20)     # 20 horas -> $264.00

# Usando función con múltiples argumentos
pago_personalizado = calcular_pago_detallado(40, 24, 0.22)  # $748.80
```

### ⭐ Consejos adicionales
1. Mantén tus funciones simples y enfocadas en una sola tarea
2. Usa nombres descriptivos que indiquen lo que hace la función
3. Documenta tus funciones cuando sea necesario
4. Verifica los valores de entrada cuando sea necesario
5. Procura que tus funciones no tengan efectos secundarios inesperados

¡Feliz programación! 🚀 