from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/gen')
def gen_random():
    with open('quotes.txt', 'r', encoding = 'utf-8') as f:
        quotes = f.readlines()
    text = ''
    while text == '':
        text = random.choice(quotes)
    return render_template('index.html', word = text)

if '__main__' == __name__:
    app.run(host="0.0.0.0")
    


