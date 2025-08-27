# Ejercicios Teóricos: Algoritmos de Ordenamiento

## Ejercicio 1: Comprensión de Bubble Sort
Considera el siguiente arreglo: [5, 2, 8, 1, 9]

a) Muestra paso a paso cómo Bubble Sort ordena este arreglo
b) ¿Cuántas comparaciones se realizaron en total?
c) ¿Cuántos intercambios fueron necesarios?
d) ¿En qué iteración se colocó el 9 en su posición final? ¿Por qué?

## Ejercicio 2: Análisis de Merge Sort
Para el arreglo [6, 2, 9, 1, 5]:

a) Dibuja el árbol de recursión completo del Merge Sort
b) Muestra el proceso de merge para combinar [2,6] y [1,9]
c) ¿Cuántas divisiones recursivas se realizaron en total?
d) ¿Cuánta memoria extra se necesitó en el peor caso?

## Ejercicio 3: Comparación de Rendimiento
Analiza los siguientes casos:

a) ¿Qué algoritmo elegirías para ordenar una lista de 10 números? ¿Por qué?
b) Para una lista de 1000 números, ¿qué algoritmo es mejor? Justifica.
c) Si la lista está casi ordenada, ¿cuál algoritmo tendría mejor desempeño?
d) Si la memoria es muy limitada, ¿qué algoritmo recomendarías?

## Ejercicio 4: Casos Especiales
Responde y justifica:

a) ¿Qué pasa si aplicamos Bubble Sort a una lista ya ordenada?
b) ¿Y si aplicamos Merge Sort a una lista en orden inverso?
c) ¿Cuál algoritmo mantiene el orden relativo de elementos iguales? ¿Por qué es esto importante?
d) Da un ejemplo práctico donde sea crucial mantener este orden relativo

# Ejercicios Adicionales: Quick Sort y Heap Sort

## Ejercicio 5: Análisis de Particionamiento
Para el arreglo [7, 2, 1, 6, 8, 5, 3, 4] usando Quick Sort:

a) Muestra el proceso de particionamiento usando el último elemento como pivote
b) ¿Cuántas comparaciones e intercambios ocurren en el primer particionamiento?
c) Dibuja el árbol de recursión completo
d) ¿Qué pasa si siempre elegimos el primer elemento como pivote y el arreglo está casi ordenado?

## Ejercicio 6: Heap Sort y Árboles Binarios
Para el arreglo [4, 10, 3, 5, 1]:

a) Dibuja el árbol binario que representa el heap inicial
b) Muestra el proceso paso a paso de la construcción del max-heap
c) ¿Cuántas comparaciones se necesitan para hacer heapify en un árbol de altura h?
d) Explica por qué la fase de construcción del heap es O(n)

## Ejercicio 7: Comparación Avanzada
Analiza y compara los cuatro algoritmos:

a) ¿Cuál es más eficiente para arreglos casi ordenados? ¿Por qué?
b) ¿Cuál maneja mejor los elementos duplicados? Explica.
c) En términos de memoria auxiliar, ordénalos de menor a mayor uso.
d) ¿Cuál elegirías para ordenar registros grandes donde los intercambios son costosos?

## Ejercicio 8: Casos Prácticos
Para cada escenario, elige el mejor algoritmo y justifica:

a) Ordenar un archivo grande en disco con memoria RAM limitada
b) Mantener ordenada una cola de prioridad que se actualiza frecuentemente
c) Ordenar un log de eventos por timestamp donde muchos eventos ocurren en el mismo segundo
d) Ordenar una lista de objetos grandes donde comparar es barato pero intercambiar es costoso
