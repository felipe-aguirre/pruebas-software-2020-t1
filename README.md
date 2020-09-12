# Tarea 1: Validación y verificación

- Autor: Felipe Aguirre
- 11 Septiembre 2020

---

## Requisitos

- Tener instalado [python 3.x](https://www.python.org/download/releases/3.0/) en su sistema operativo

---

## Contenido

- Archivo `function.py`que contiene la función a evaluar `compareString(A,B)`cuya función es detemrinar que string es más largo entre `A` y `B`
- Archivo `test_cases.py `:Diseñado para realizar las pruebas a la función `compareString()`

---

## Instrucciones

- Editar el archivo `test_cases.py`: Modificar la lista `cases`de la linea `15` por una lista de tuplas con los pares de parámetros de prueba

  ```python
  cases = [("Sol", "Luna"), ("Dia", "NOCHE"), (3,"test"), ("Buenas", 5), (6,8)]
  # Reemplazar por la lista de tuplas que se deseen probar
  ```

- Ubicar los archivios `function,py`y `test_cases.py`en el mismo directorio

- Ejecutar `test_cases.py`con el intérprete Python

- Se generará un LOG en el mismo directorio base, llamado `debug.log`que contiene el detalle de las pruebas realizadas

---

## Supuestos

- El programa está diseñado para recibir solo 2 argumentos, es decir, la tupla de cada prueba solo puede contener 2 elementos.

