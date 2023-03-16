from flask import Flask, render_template, request
from openai import generer_bilde
from dotenv import dotenv_values

env = dotenv_values(".env")
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        try:
            tekst = request.form["tekst"]
            bilder = generer_bilde(tekst, env["API_KEY"])
            return render_template("index.html", bilder=bilder, tekst=tekst)
        except:
            return render_template("index.html", bilder=[], tekst="Ukjent feil. Prøv igjen")
    else:
        return render_template("index.html", bilder=[], tekst="Thors bildegenerator")
