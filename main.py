from flask import Flask, request, render_template
import pandas as pd
import os

# ✅ APP TEM QUE SER CRIADO PRIMEIRO
app = Flask(__name__)

# ======================
# ROTA HOME
# ======================
@app.route("/")
def index():
    return """
    <h1>🚚 Sistema de Fretes – Zé Delivery</h1>
    <p>Site rodando corretamente.</p>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="arquivo" accept=".xlsx" required>
        <br><br>
        <button type="submit">Processar XLSX</button>
    </form>
    """

# ======================
# ROTA UPLOAD (XLSX)
# ======================
@app.route("/upload", methods=["POST"])
def upload():
    arquivo = request.files.get("arquivo")

    if not arquivo or not arquivo.filename.endswith(".xlsx"):
        return "Arquivo inválido. Envie um XLSX.", 400

    try:
        df = pd.read_excel(arquivo)
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}", 500

    # Normaliza colunas
    df.columns = [c.strip().lower() for c in df.colu]()
