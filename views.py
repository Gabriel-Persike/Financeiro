from main import app
from flask import render_template
from flask import request

from models import POST_ENTRADA, GET_ENTRADAS


# Rotas
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/entradas", methods = ["GET", "POST"])
def entradas():
    if request.method == "GET":
        entradas  = GET_ENTRADAS()
        return render_template("entradas.html", entradas = entradas)

    elif request.method == "POST":
        data = request.form
        retorno = POST_ENTRADA(data)
        if retorno != True: 
            return render_template("entradas.html", errorMessage = retorno)
        else:
            return render_template("entradas.html")






