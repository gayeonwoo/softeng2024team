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
    return "HEllo World!!"

@app.route("/kcal/")
def kcal():
    food=request.args.get('food')
    amount=request.args.get('amount')
    if find_kcal(food,amount)==None:
        return f"{food}의 열량 정보가 없습니다."
    else:
        return f"{food} {amount}g : {find_kcal(food,amount)}kcal"


app.run(debug=True)