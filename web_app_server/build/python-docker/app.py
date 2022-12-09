import pickle

import pandas as pd
from flask import Flask, flash, render_template, request
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
# not secret, this is needed for flash()
app.config["SECRET_KEY"] = "28185ab68f8cb88d4a7f09d7cc9ed27616d610a23be767dc"
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/data", methods=["POST", "GET"])
def result():
    if request.method == "GET":
        return "The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == "POST":
        if len(request.form) == 21:
            df = pd.DataFrame([request.form])
            high_risk = int(loaded_model.predict(df)[0])
            if high_risk:
                results = "The model predicts a high risk of heart disease."
            else:
                results = "The model doesn't predict a high risk of heart disease."
            return render_template("data.html", results=results)
        else:
            flash("Please fill out the form.")
            return render_template("form.html")


with open("./tree_balanced.model", "rb") as f:
    loaded_model = pickle.load(f)

if __name__ == "__main__":
    app.run(debug=True)
