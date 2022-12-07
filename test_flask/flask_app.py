import pickle

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/data", methods=["POST", "GET"])
def result():
    if request.method == "GET":
        return "The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == "POST":
        df = pd.DataFrame([request.form])
        high_risk = int(loaded_model.predict(df)[0])
        if high_risk:
            results = "The model predicts a high risk of heart disease."
        else:
            results = "The model doesn't predict a high risk of heart disease."
        return render_template("data.html", results=results)


with open("models/tree_balanced.model", "rb") as f:
    loaded_model = pickle.load(f)

app.run(debug=True)
