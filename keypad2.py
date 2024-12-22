import RPi.GPIO as GPIO
import time

# 4x4 키패드 매트릭스 구성
matrix_keys = [['1', '2', '3', 'A'],
               ['4', '5', '6', 'B'],
               ['7', '8', '9', 'C'],
               ['*', '0', '#', 'D']]

keypad_rows = [9, 8, 7, 6]  # ROW 핀 번호
keypad_columns = [5, 4, 3, 2]  # COL 핀 번호
row_pins = []
col_pins = []

# 비밀번호 입력값을 저장할 임시 변수
guess = []
# 잠금 비밀번호 (6자리)
secret_pin = ['1', '2', '3', '4', '5', '6']
# 비밀번호 성공시 LED On (15번 핀 사용)
led = 15

# GPIO 설정
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

# ROW 핀 설정
for x in range(4):
    row_pins.append(keypad_rows[x])
    GPIO.setup(row_pins[x], GPIO.OUT)
    GPIO.output(row_pins[x], GPIO.HIGH)

# COL 핀 설정
for x in range(4):
    col_pins.append(keypad_columns[x])
    GPIO.setup(col_pins[x], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# 키패드 입력 함수
def scankeys():
    global guess
    for row in range(4):
        GPIO.output(row_pins[row], GPIO.LOW)  # 현재 row를 LOW로 설정하여 활성화
        for col in range(4):
            if GPIO.input(col_pins[col]) == GPIO.HIGH:  # 버튼이 눌렸는지 확인
                key = matrix_keys[row][col]
                print("You have pressed:", key)
                time.sleep(0.3)  # 디바운싱
                guess.append(key)  # 입력값 저장
                if len(guess) == 6:  # 6자리 비밀번호 입력 완료
                    checkPin(guess)
                    guess = []  # 비밀번호 입력 초기화
        GPIO.output(row_pins[row], GPIO.HIGH)  # current row를 다시 HIGH로 설정

# 입력한 번호 체크 함수
def checkPin(guess):
    if guess == secret_pin:
        print("문열림")
        GPIO.output(led, GPIO.HIGH)  # LED를 켜서 잠금 장치를 열도록 할 수 있습니다.
        time.sleep(3)
        GPIO.output(led, GPIO.LOW)  # LED를 끄기
    else:
        print("비번틀림")

# 프로그램 시작
print("비밀번호 6자리 입력")
try:
    while True:
        scankeys()
finally:
    GPIO.cleanup()  # 프로그램 종료 시 GPIO 핀 정리
