from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    
    if request.method == "POST":
        req = request.form
        question = req["question"]
        print(question)
        return redirect(request.url)

    return render_template("site.html")

app.run(host='0.0.0.0', port=8080)