from machine import Pin
import utime

# 4x4 키패드 매트릭스 구성
matrix_keys = [['1', '2', '3', 'A'],
               ['4', '5', '6', 'B'],
               ['7', '8', '9', 'C'],
               ['*', '0', '#', 'D']]
keypad_rows = [9,8,7,6]
keypad_columns = [5,4,3,2]
col_pins = []
row_pins = []

# 비번 입력값 저장할 임시 변수
guess = []
# 잠금 비밀 번호 
secret_pin = ['1','2','3','4','5','6']
# 비번 성공시 LED On (15번핀 사용)
led = Pin(15, Pin.OUT, Pin.PULL_UP)

for x in range(0,4):
    row_pins.append(Pin(keypad_rows[x], Pin.OUT))
    row_pins[x].value(1)
    col_pins.append(Pin(keypad_columns[x], Pin.IN, Pin.PULL_DOWN))
    col_pins[x].value(0)

# 키패드 입력 함수      
def scankeys():    
    for row in range(4):
        for col in range(4): 
            row_pins[row].high()
            key = None            
            if col_pins[col].value() == 1:
                print("You have pressed:", matrix_keys[row][col])
                key_press = matrix_keys[row][col]
                utime.sleep(0.3)
                guess.append(key_press)             
            if len(guess) == 6:
                checkPin(guess)
                for x in range(0,6):
                    guess.pop()
        row_pins[row].low()

# 입력한 번호 체크 함수
def checkPin(guess):
    if guess == secret_pin:
        print("문열림")
        led.value(1) # LED 대신 잠금 장치 제어로 변경
        utime.sleep(3)
        led.value(0)
    else:
        print("비번틀림")     
        
print("비밀번호 6자리 입력")
while True:   
    scankeys()
