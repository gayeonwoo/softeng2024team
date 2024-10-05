from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gyPage')
def gy():
    return render_template('gyPage.html',title='gayeon Page')

@app.route('/kmpage')
def km():
    return render_template('kmpage.html',title='KyungMun')

app.run(debug=True)