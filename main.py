from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    if not file:
        return "Nenhum arquivo enviado", 400

    df = pd.read_excel(file)

    total_entregas = len(df)
    total_valor = round(
        df.select_dtypes(include="number").sum().sum(), 2
    )

    dados = df.fillna("").to_dict(orient="records")

    return render_template(
        "resultado.html",
        total_entregas=total_entregas,
        total_valor=total_valor,
        dados=dados
    )

if __name__ == "__main__":
    app.run(debug=True)
