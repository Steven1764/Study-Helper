from flask import Flask, render_template, request, redirect
from google import genai

client = genai.Client(api_key="AIzaSyCVzkxj-cILYUUBBnNndrQLbFWvx2Hlqp8")

app = Flask(__name__)
def makeAnswer(question):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=question
    )
    return response.text
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        req = request.form
        question = req["question"]
        print(question)
        answer = makeAnswer(question)
        return render_template("site.html", answer=answer,askIA="Ask IA again")

    return render_template("site.html", answer="",askIA="Ask IA")

app.run(host='0.0.0.0', port=8080)
