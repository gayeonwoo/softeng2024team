from flask import Flask,request
from markupsafe import escape

def read_file(filename):
    kcal_dic={}
    with open(filename,encoding="utf-8-sig")as f:
        lines=f.readlines()
        for line in lines[1:]:
            food=line.split(",")[0]
            kcal_dic[food]=float(line.split(",")[1])
    return kcal_dic

def find_kcal(food,amount):
    total_kcal=0
    kcal_dic=read_file("calorie_db.csv")
    if food in kcal_dic:
        total_kcal=kcal_dic[food]/100*float(amount)
        return total_kcal
    else:
        return None

app=Flask(__name__)

@app.route("/")
def hello():
    html_str = """
    <!DOCTYPE html>
    <html lang="kr">

    <head>
    <meta charset="UTF-8">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <h1>칼로리 계산기</h1>
    </head>

    <body>
    <form id="form_id" action="javascript:post_query()">
    <label>
    섭취음식
    <input type="text" name="food">
    <br><br>
    섭취량(g)
    <input type="text" name="amount">
    <br><br>
    </label>
    <button type="submit">계산</button>
    </form>

    <div id="results"></div>

    <script>
    function post_query() {
    $.ajax({
    type: "GET",
    url: "http://127.0.0.1:5000/kcal/",
    data: $("#form_id").serialize(),
    success: update_result,
    dataType: "html"
    });
    }

    function update_result(data) {
    $("#results").html(data);
    }
    </script>
    </body>

    </html>
    """
    return html_str

@app.route("/kcal/")
def kcal():
    food=request.args.get('food')
    amount=request.args.get('amount')
    if find_kcal(food,amount)==None:
        return f"{food}의 열량 정보가 없습니다."
    else:
        return f"{food} {amount}g : {find_kcal(food,amount)}kcal"

app.run(debug=True)
