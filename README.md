Integrando todo
===============

1-Uso de Linter (PEP8)
--------------------

Utilizar pylint pra detectar errores de estilo, nombres de variables, 
comentarios no claros y largas lineas de código.

2-Uso de Profilers
----------------

Usando cProfile identificar las funciones que demoran mas tiempo y ver si se 
puede optimizar el código

3-Diagrama de Pareto
--------------------
Con los resultados obtenidos del pylint marcar la frecuencia de los problems y 
dibujar el diagrama, identificar las partes mejorar.

Se podrían agrupar en lo siguientes problemas:

Problemas de rendimiento
Problemas de estilo PEP8
Problemas de organización del código

4-Ejemplos de optimización de la función de fibonacci
-----------------------------------------------------

Memoización (Optimización con Cache)

"""
def fibonacci_memo(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci_memo(n - 1, cache) + fibonacci_memo(n - 2, cache)
    return cache[n]
"""

Iterativo (En lugar de recursivo)

"""
def fibonacci_iterativo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
"""

Programación Dinámica (Bottom-Up)

"""
def fibonacci_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
"""


