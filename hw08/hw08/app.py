from flask import Flask, render_template
import pandas as pd

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gyPage')
def gy():
    df=pd.read_csv("static/gydata.csv")
    post_list=[]
    for i, row in df.iterrows():
        post_list.append({
            "title":row["title"],
            "content":row["content"]
        })
    return render_template('gyPage.html',title='gayeon Page', posts=post_list)

@app.route('/kmpage')
def km():
    df = pd.read_csv("kmdata.csv")
    post_list = df.to_dict(orient='records')
    print(post_list)
    return render_template('kmpage.html',title='KyungMun', posts=post_list)

app.run(debug=True)
