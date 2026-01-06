
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return "Nenhum arquivo enviado", 400

    df = pd.read_excel(file)

    tabela_html = df.to_html(classes="ze-table", index=False, border=0)
    return render_template("resultado.html", tabela=tabela_html)

if __name__ == "__main__":
    app.run(debug=True)
