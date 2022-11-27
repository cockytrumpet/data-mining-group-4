from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World" #This will display hello world on a web page, required double quotes to work for some reason!


if __name__ == '__main__':
   app.run()
