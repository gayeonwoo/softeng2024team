from flask import Flask, request, render_template_string
from markupsafe import escape


def read_file(filename):
    kcal_dic = {}
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:  # 첫 줄은 헤더이므로 건너뜀
            food = line.split(",")[0]
            kcal_dic[food] = float(line.split(",")[1])
    return kcal_dic


def find_kcal(food, amount):
    total_kcal = 0
    kcal_dic = read_file("calorie_db.csv")
    if food in kcal_dic:
        total_kcal = kcal_dic[food] / 100 * float(amount)
        return total_kcal
    else:
        return None


app = Flask(__name__)


# 기본 경로에 바로 칼로리 계산기를 연결
@app.route("/", methods=["GET", "POST"])  # 기본 경로를 /로 수정
def kcal():
    html_code = '''
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>칼로리 계산기</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 50px;
            }
            form {
                margin-bottom: 30px;
            }
        </style>
    </head>
    <body>
        <h1>칼로리 계산기</h1>
        <form action="/" method="POST">  <!-- action 경로를 /로 수정 -->
            <label for="food">음식 이름:</label><br>
            <input type="text" id="food" name="food" required><br><br>
            <label for="amount">양 (g):</label><br>
            <input type="number" id="amount" name="amount" required><br><br>
            <input type="submit" value="칼로리 계산하기">
        </form>

        {% if result %}
            <div style="margin-top: 20px;">
                <h2>결과</h2>
                <p>{{ result }}</p>
            </div>
        {% endif %}
    </body>
    </html>
    '''

    if request.method == "POST":
        food = request.form.get('food')
        amount = request.form.get('amount')
        kcal_info = find_kcal(food, amount)
        if kcal_info is None:
            result_message = f"{food}의 열량 정보가 없습니다."
        else:
            result_message = f"{food} {amount}g : {kcal_info}kcal"
        return render_template_string(html_code, result=result_message)

    return render_template_string(html_code, result=None)


if __name__ == "__main__":
    app.run(debug=True)
