import requests

def send_id_to_server(id_number):
    url = 'http://127.0.0.1:8000/management/'  # 실제 Django 서버 IP로 변경
    response = requests.post(url, data={'id_number': id_number})
    if response.status_code == 200:
        print("성공적으로 데이터가 서버로 전송되었습니다.")
    else:
        print("서버로 데이터 전송 실패")
