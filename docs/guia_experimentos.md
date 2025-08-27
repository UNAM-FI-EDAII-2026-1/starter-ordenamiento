# Guía de Experimentos: Análisis Empírico de Algoritmos de Ordenamiento

## Objetivo
Realizar un análisis experimental comparativo entre Bubble Sort y Merge Sort, verificando empíricamente sus complejidades teóricas y comportamiento en diferentes escenarios.

## Experimentos Requeridos

### 1. Análisis de Tiempo vs Tamaño
- Utiliza la función `generate_random_data` de `test_utils.py`
- Mide tiempos para tamaños: [100, 200, 300, 400, 500, ..., 100000] asi es de 100 en 100 hasta 100000.
- Grafica tiempo vs tamaño para ambos algoritmos
- Compara con la complejidad teórica

### 2. Análisis de Casos
Para cada algoritmo, mide y compara tiempos con:
- Arreglos aleatorios
- Arreglos casi ordenados (usa `generate_nearly_sorted`)
- Arreglos inversamente ordenados (usa `generate_reversed`)
- Tamaño fijo: 5000 elementos
- Grafica los resultados en un diagrama de barras

## Formato de Entrega

### Reporte (PDF, máximo 5 páginas)
1. Introducción y Metodología
2. Resultados y Gráficas
   - Usa matplotlib o seaborn
   - Incluye barras de error
   - Etiqueta ejes y unidades
3. Análisis
   - Compara con complejidad teórica
   - Explica discrepancias
   - Analiza trade-offs
4. Conclusiones

### Código
- Gráficas generadas
- Datos recolectados
- Debe venir en el reporte de no mas 5 pags, por cada pag extra les bajo puntos por hoja. aprox 1.5 por extra hoja.

## Experimentos Adicionales para Quick Sort y Heap Sort

### 3. Análisis de Estrategias de Pivote
Para Quick Sort, implementa y compara:
- Pivote como último elemento
- Pivote aleatorio
- Pivote como mediana de tres
- Mide tiempos para cada estrategia con diferentes tipos de entrada
- Grafica comparando las tres estrategias

### 4. Análisis de Construcción de Heap
Para Heap Sort:
- Mide el tiempo de construcción inicial del heap vs. tamaño
- Compara tiempo de heapify vs. altura del árbol
- Analiza el número de intercambios en diferentes fases

### 5. Comparación de los 4 Algoritmos
- Compara todos los algoritmos implementados
- Usa conjuntos de datos de tamaño grande (>50000 elementos)
- Mide:
  * Tiempo de ejecución
  * Número de comparaciones
  * Número de intercambios
  * Uso de memoria
- Genera gráficas comparativas

### 6. Análisis de Estabilidad
- Implementa un experimento que demuestre la estabilidad/inestabilidad
- Usa registros con claves duplicadas
- Documenta el comportamiento de cada algoritmo

## Rúbrica Final
- Implementación correcta (20%)
- Experimentos básicos (20%)
- Experimentos avanzados (20%)
- Análisis de resultados (20%)
- Calidad del reporte (20%)
