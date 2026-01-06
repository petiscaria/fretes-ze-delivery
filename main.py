from flask import Flask, render_template, request
import csv
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    entregas = []
    total_valor = 0
    total_qtd = 0

    if request.method == "POST":
        file = request.files.get("file")

        if file and file.filename.endswith(".csv"):
            stream = io.StringIO(file.stream.read().decode("utf-8"), newline=None)
            reader = csv.DictReader(stream)

            for row in reader:
                valor = float(row.get("valor", 0))
                entregas.append({
                    "data": row.get("data"),
                    "entregador": row.get("entregador"),
                    "valor": valor
                })
                total_valo_
