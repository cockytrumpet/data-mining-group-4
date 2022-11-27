from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World" #This will display hello world on a web page, required double quotes to work for some reason!


@app.route('/prediction')
def prediction():
    return "Your prediction will appear here. Add model code such that it runs the formula and outputs in this box"

if __name__ == '__main__':
   app.run(debug = True)