from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html', shortcode=request.args['shortcode'])

if __name__ == '__main__':
   app.run(debug = True)