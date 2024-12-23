from gpiozero import DigitalOutputDevice, DigitalInputDevice
from time import sleep
import requests  # HTTP 요청을 보내기 위한 라이브러리

# 키패드 핀 설정
R1 = DigitalOutputDevice(29)
R2 = DigitalOutputDevice(31)
R3 = DigitalOutputDevice(33)
R4 = DigitalOutputDevice(35)

C1 = DigitalInputDevice(32, pull_up=False)
C2 = DigitalInputDevice(36, pull_up=False)
C3 = DigitalInputDevice(38, pull_up=False)
C4 = DigitalInputDevice(40, pull_up=False)

AUTHORIZED_USERS = {
    "123456789": {"name": "김철수", "role": "관리자"},
    "234567890": {"name": "이영희", "department": "재배담당"},
    "345678901": {"name": "박지성", "department": "품질관리"}
}

class Keypad:
    def __init__(self):
        self.current_input = ""

    def scan_keypad(self, row_pin, characters):
        """키패드 한 행을 스캔하고 눌린 키를 반환"""
        row_pin.on()
        pressed_key = None

        if C1.value:
            pressed_key = characters[0]
        elif C2.value:
            pressed_key = characters[1]
        elif C3.value:
            pressed_key = characters[2]
        elif C4.value:
            pressed_key = characters[3]

        row_pin.off()
        return pressed_key

    def get_pressed_key(self):
        """모든 행을 스캔하여 눌린 키를 확인"""
        keys = [
            self.scan_keypad(R1, ["1", "2", "3", "A"]),
            self.scan_keypad(R2, ["4", "5", "6", "B"]),
            self.scan_keypad(R3, ["7", "8", "9", "C"]),
            self.scan_keypad(R4, ["*", "0", "#", "D"])
        ]
        return next((key for key in keys if key is not None), None)

    def verify_user(self):
        """사용자 ID 확인 및 접근 권한 검증"""
        if len(self.current_input) == 9:  # 9자리 입력 완료
            if self.current_input in AUTHORIZED_USERS:
                return {"status": "success", "user_id": self.current_input}
            else:
                return {"status": "failure", "user_id": self.current_input}
        return None

    def run(self):
        """메인 실행 루프"""
        while True:
            key = self.get_pressed_key()
            if key:
                if key in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    self.current_input += key
                elif key == "#":
                    self.current_input = ""
                elif key == "*":
                    if len(self.current_input) == 9:
                        user_data = self.verify_user()
                        if user_data:
                            # 서버에 요청 보내기
                            response = requests.post("http://127.0.0.1:8000/greenhouse/access/", data=user_data)
                            print(response.text)  # 서버로부터 받은 응답 출력
                        self.current_input = ""  # 입력 초기화
                sleep(0.2)  # 디바운싱

if __name__ == "__main__":
    keypad = Keypad()
    keypad.run()
