from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gyPage')
def gy():
    return render_template('gyPage.html')

@app.route('/kmpage')
def km():
    return render_template('kmpage.html')

app.run(debug=True)