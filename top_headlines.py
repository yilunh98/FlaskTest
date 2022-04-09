from flask import Flask,render_template
import requests
from secret import api_key

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name=nm)

@app.route('/headlines/<nm>')
def headline(nm):
    url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=' + api_key
    response = requests.get(url).json()['results'][:5]
    return render_template('headlines.html', name=nm, stories=response)

@app.route('/links/<nm>')
def link(nm):
    url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=' + api_key
    response = requests.get(url).json()['results'][:5]
    return render_template('links.html', name=nm, stories=response)

@app.route('/images/<nm>')
def image(nm):
    url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=' + api_key
    response = requests.get(url).json()['results'][:5]
    return render_template('images.html', name=nm, stories=response)

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)