from flask import Flask, render_template

TEMPLATE = './templates'

STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC )

@app.route('/')
def helloWorld():
    return 'hello World'

@app.route('/home')
def home():
    return render_template('home.html')

##app.run(host='0.0.0.0', port=5000)