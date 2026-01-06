from flask import Flask, request, render_template
import pandas as pd
import csv
import io

@app.route("/upload", methods=["POST"])
def upload():
    arquivo = request.files.get("arquivo")

    if not arquivo or not arquivo.filename.endswith(".xlsx"):
        return "Arquivo inválido. Envie um XLSX.", 400

    try:
        df = pd.read_excel(arquivo)
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}", 500

    # 🔧 NORMALIZA NOMES DAS COLUNAS
    df.columns = [c.strip().lower() for c in df.columns]

    total_entregas = len(df)

    # 🔧 TRATA VALOR (vírgula, vazio, NaN)
    if "valor" in df.columns:
        df["valor"] = (
            df["valor"]
            .astype(str)
            .str.replace(",", ".", regex=False)
        )
        df["valor"] = pd.to_numeric(df["valor"], errors="coerce").fillna(0)
        total_valor = df["valor"].sum()
    else:
        total_valor = 0

    dados = df.fillna("").to_dict(orient="records")

    return render_template(
        "resultado.html",
        total_entregas=total_entregas,
        total_valor=f"{total_valor:.2f}",
        dados=dados
    )
