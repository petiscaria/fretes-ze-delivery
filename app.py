from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return render_template("index.html")
        file = request.files["file"]
        if file.filename == "":
            return render_template("index.html")
        df = pd.read_excel(file)
        return render_template("index.html", columns=df.columns, rows=df.head(10).values)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
