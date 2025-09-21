# archivo: test_sistema.py
import pytest
from sistema import promedio, procesar_estudiantes

def test_promedio_basico():
    assert promedio([10, 8, 6]) == 8.0
    assert promedio([]) == 0.0
    assert promedio([7]) == 7.0
    assert promedio([9.5, 8.25]) == 8.88  # redondeo a 2 decimales

def test_procesar_orden_y_campos():
    estudiantes = [
        {"nombre": "Ana", "apellido": "García", "dni": "123", "edad": 20, "notas": [9, 8, 10]},
        {"nombre": "Luis", "apellido": "Pérez", "dni": "456", "edad": 22, "notas": [6, 7, 5]},
        {"nombre": "Marta", "apellido": "López", "dni": "789", "edad": 21, "notas": [10, 9, 9]}
    ]
    res = procesar_estudiantes(estudiantes)
    # Orden: Marta (9.33), Ana (9.0), Luis (6.0)
    assert [r["dni"] for r in res] == ["789", "123", "456"]
    assert res[0]["promedio"] == 9.33
    assert res[1]["edad"] == 20
