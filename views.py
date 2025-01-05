from main import app
from flask import render_template
from flask import request

from models import POST_ENTRADA


# Rotas
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/entradas", methods = ["GET", "POST"])
def entradas():
    if request.method == "GET":
        return render_template("entradas.html")

    elif request.method == "POST":
        data = request.form
        print(data)
        POST_ENTRADA(data)
        return render_template("entradas.html")




