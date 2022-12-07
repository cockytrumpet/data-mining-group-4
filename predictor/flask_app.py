# from flask import Flask, render_template, request
# app = Flask(__name__)

# @app.route('/', methods =["GET", "POST"])
# def home():
#    return render_template('home.html')


# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    return render_template('result_value.html')

# if __name__ == '__main__':
#    app.run(debug = True)

import pickle

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/form")
def form():
    return render_template("home.html")


@app.route("/data/", methods=["POST", "GET"])
def data():
    if request.method == "GET":
        return "The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == "POST":
        form_data = request.form
        df = pd.DataFrame([form_data])
        high_risk = int(loaded_model.predict(df)[0])
        if high_risk:
            results = "The model predicts a high risk of heart disease."
        else:
            results = "The model doesn't predict a high risk of heart disease."
        return render_template("result_value.html", results=results)


with open("../models/tree_balanced.model", "rb") as f:
    loaded_model = pickle.load(f)

app.run(host="localhost", port=5000)