from flask import Flask, request, render_template
import pandas as pd
import csv
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    total_entregas = None
    total_valor = None
    dados = []

    if request.method == "POST":
        arquivo = request.files.get("arquivo")

        if arquivo:
            stream = io.StringIO(arquivo.stream.read().decode("utf-8"))
            leitor = csv.DictReader(stream)

            total_entregas = 0
            total_valor = 0

            for linha in leitor:
                total_entregas += 1
                valor = float(linha.get("valor", 0))
                total_valor += valor

                dados.append({
                    "data": linha.get("data", ""),
                    "entregador": linha.get("entregador", ""),
                    "valor": f"{valor:.2f}"
                })

            total_valor = f"{total_valor:.2f}"

    return render_template(
        "index.html",
        total_entregas=total_entregas,
        total_valor=total_valor,
        dados=dados
    )

if __name__ == "__main__":
    app.run(debug=True)
