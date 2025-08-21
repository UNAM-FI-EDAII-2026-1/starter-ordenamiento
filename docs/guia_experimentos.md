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

## Rúbrica
- Completitud de experimentos (30%)
- Calidad de gráficas (20%)
- Análisis de resultados (30%)
- Conclusiones fundamentadas (20%)
