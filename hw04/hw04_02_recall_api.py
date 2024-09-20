from flask import Flask,request
from markupsafe import escape

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!!</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}"

@app.route("/gugudan/")
def gugudan():
    dan=request.args.get('dan')
    html_str=""
    for i in range(1,10):
        html_str+=f"<br>{dan}x{i}=<strong>{int(dan)*i}</strong>"
    return f"{dan}단 출력중...<br>{html_str}"

@app.route("/findgugu")
def gugu():
    html_str="""
    <!DOCTYPE html>
    <html lang="kr">

    <head>
    <meta charset="UTF-8">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <title>Flask HOme Page</title>
    </head>

    <body>
    <form id="form_id" action="javascript:post_query()">
    <h2>구구단 출력하기</h2>
    <label>
    단:
    <input type="text" name="dan">
    </label>
    <button type="submit">Go</button>
    </form>

    <div id="results"></div>

    <script>
    function post_query(){
    $.ajax({
    type:"GET",
    url:"http://127.0.0.1:5000/gugudan/",
    data:$("#form_id").serialize(),
    success:update_result,
    dataType:"html"})}

    function update_result(data){
    $("#results").html(data)}
    </script>
    </body>

    </html>
    """
    return html_str

app.run(debug=True)