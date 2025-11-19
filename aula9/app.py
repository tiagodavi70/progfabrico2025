from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Olá mundo"

@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        
        return render_template("resultado.html", nome=nome, email=email)
    return render_template("formulario.html") 


if __name__ == "__main__":
    app.run(debug=True)