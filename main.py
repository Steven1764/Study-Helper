from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        req = request.form
        question = req["question"]
        print(question)
        answer = "This is gona be working when i get my API key trust"

        return render_template("site.html", answer=answer,askIA="Ask IA again")

    return render_template("site.html", answer="",askIA="Ask IA")

app.run(host='0.0.0.0', port=8080)
