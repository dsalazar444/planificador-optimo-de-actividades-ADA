# Planificador Óptimo de Actividades

## Descripción

Este proyecto implementa un **planificador inteligente de actividades** que utiliza el algoritmo de **backtracking** para encontrar la mejor combinación de actividades sin conflictos de horario, maximizando la prioridad total.

## Problema

Dado un conjunto de actividades con:
- Hora de inicio y finalización
- Nivel de prioridad (1=baja, 2=media, 3=alta)

**Objetivo**: Seleccionar el máximo número de actividades sin solapamientos que maximice la prioridad total.

## Solución: Algoritmo de Backtracking

El algoritmo explora recursivamente todas las combinaciones posibles de actividades:

1. **Decisión 1**: Saltar la actividad actual
2. **Decisión 2**: Incluir la actividad si no causa conflictos de horario

Por cada nodo del árbol de búsqueda, se verifica que la nueva actividad comience después de que la última seleccionada haya finalizado.

## Estructura del Proyecto

### Clases

#### `Activity`
Representa una actividad individual.
- **Atributos**:
  - `id`: Identificador único (auto-incrementado)
  - `title`: Nombre de la actividad
  - `start_hour`: Hora de inicio (formato 24h con decimales, ej: 14.45)
  - `finish_hour`: Hora de finalización
  - `priority`: Nivel de prioridad (1, 2 o 3)

#### `Planner`
Resuelve el problema de planificación mediante backtracking.
- **Métodos principales**:
  - `order_by_start_hour()`: Ordena actividades por hora de inicio
  - `backtracking()`: Busca recursivamente la mejor solución
  - `print_best_solution()`: Muestra resultados con estadísticas

### Archivo Principal: `main.py`
Interfaz interactiva que:
- Solicita actividades al usuario
- Valida entrada de datos
- Ejecuta el planificador
- Muestra la solución óptima

## Cómo Usar

### Ejecución
```bash
python main.py
```

### Entrada de Datos
1. **Título**: Nombre descriptivo de la actividad
2. **Hora de inicio**: Formato `hora.minutos` (ej: `9.30` para 9:30)
3. **Hora de finalización**: Mismo formato
4. **Prioridad**: Número entre 1 y 3
   - `1` = Baja
   - `2` = Media
   - `3` = Alta

Escribe `salir` en el título para terminar de ingresar actividades.

### Ejemplo de Ejecución
```
PLANIFICADOR ÓPTIMO DE ACTIVIDADES
===================================

Título: Reunión con equipo
  Hora de inicio (ej: 9.30 para 9:30, 14.45 para 14:45): 9.30
  Hora de finalización (ej: 9.30 para 9:30, 14.45 para 14:45): 10.30
  Prioridad (1=baja, 2=media, 3=alta): 3
✓ Actividad agregada

...

MEJOR SOLUCIÓN ENCONTRADA
==========================

Estadísticas:
  • Actividades totales: 5
  • Actividades seleccionadas: 3
  • Actividades descartadas: 2

Actividades seleccionadas:
  ID: 1
    Título: Reunión con equipo
    Horario: 9.3 - 10.3
    Prioridad: 3
...
```

## Complejidad Temporal

- **Peor caso**: O(2^n) donde n es el número de actividades
- Las actividades se ordena previamente: O(n log n)
- El backtracking explora todas las combinaciones posibles

## Requisitos

- Python 3.7+
- Sin dependencias externas

## Notas Técnicas

- Las actividades se procesan en orden de hora de inicio para optimizar la búsqueda
- Las horas se manejan como números flotantes (14.45 = 14:45)
- El algoritmo garantiza encontrar la solución óptima exploración completa
