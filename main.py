@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("POST RECEBIDO")

        if "file" not in request.files:
            print("ERRO: request.files vazio")
            return render_template("index.html")

        file = request.files["file"]

        if file.filename == "":
            print("ERRO: filename vazio")
            return render_template("index.html")

        print("Arquivo recebido:", file.filename)

        df = pd.read_excel(file)
        print("Excel lido com sucesso")

    return render_template("index.html")
