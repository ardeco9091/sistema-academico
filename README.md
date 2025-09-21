# Sistema Académico (Promedios + Ordenamiento) 🎓

API y librería en Python que:
- Calcula **promedio** por estudiante (2 decimales).
- **Ordena** estudiantes de **nota más alta a más baja**.
- Devuelve **nombre, apellido, DNI, edad y promedio**.

## 📦 Estructura
- `sistema.py` → lógica de negocio.
- `app.py` → API Flask (`/` y `/estudiantes`).
- `test_sistema.py` → pruebas unitarias con `pytest`.
- `requirements.txt` → dependencias.
- `Procfile` → arranque en Heroku.
- `render.yaml` → despliegue rápido en Render.
- `sample_request.json` → ejemplo de payload.

## ▶️ Uso local
```bash
pip install -r requirements.txt
pytest -q
python app.py
```
Probar endpoint:
```bash
curl -X POST http://127.0.0.1:5000/estudiantes \
  -H "Content-Type: application/json" \
  -d @sample_request.json
```

## ☁️ Despliegue en Render (recomendado)
1. Subí este repo a GitHub.
2. En Render → "New Web Service" → conecta tu repo.
3. Elige un Runtime **Python 3.11+**.
4. **Build command**: `pip install -r requirements.txt`
5. **Start command**: `gunicorn app:app`
6. Añadí la variable `PYTHON_VERSION=3.11` si es necesario.

## ☁️ Despliegue en Heroku
```bash
heroku create sistema-academico
git push heroku main
heroku ps:scale web=1
heroku open
```

## 💉 Ejemplo de payload
```json
{
  "estudiantes": [
    {
      "nombre": "Ana",
      "apellido": "García",
      "dni": "12345678",
      "edad": 20,
      "notas": [
        9,
        8,
        10
      ]
    },
    {
      "nombre": "Luis",
      "apellido": "Pérez",
      "dni": "87654321",
      "edad": 22,
      "notas": [
        6,
        7,
        5
      ]
    },
    {
      "nombre": "Marta",
      "apellido": "López",
      "dni": "11223344",
      "edad": 21,
      "notas": [
        10,
        9,
        9
      ]
    }
  ]
}
```

## ✅ Respuesta esperada
Lista de estudiantes **ordenada** por `promedio` (descendente).
