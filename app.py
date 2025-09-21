# archivo: app.py
from flask import Flask, request, jsonify
from sistema import procesar_estudiantes

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return jsonify({"status": "ok", "mensaje": "API de Sistema Académico lista"})

@app.route("/estudiantes", methods=["POST"])
def calcular():
    data = request.get_json(silent=True) or {}
    estudiantes = data.get("estudiantes", [])
    try:
        resultado = procesar_estudiantes(estudiantes)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
