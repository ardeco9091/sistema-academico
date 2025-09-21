# archivo: sistema.py
from typing import List, Dict, Any

def promedio(notas: List[float]) -> float:
    """Devuelve el promedio de una lista de notas (0 si está vacía)."""
    return round(sum(notas) / len(notas), 2) if notas else 0.0

def procesar_estudiantes(estudiantes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Enriquecemos cada estudiante con su promedio y ordenamos de mayor a menor.
    Espera claves: nombre, apellido, dni, edad, notas (lista de números).
    """
    resultado = []
    for e in estudiantes:
        prom = promedio(e.get("notas", []))
        resultado.append({
            "nombre": e.get("nombre", "").strip(),
            "apellido": e.get("apellido", "").strip(),
            "dni": str(e.get("dni", "")).strip(),
            "edad": int(e.get("edad", 0)),
            "promedio": prom
        })
    resultado.sort(key=lambda x: x["promedio"], reverse=True)
    return resultado
