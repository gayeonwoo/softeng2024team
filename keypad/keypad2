from gpiozero import DigitalOutputDevice, DigitalInputDevice
from time import sleep
from datetime import datetime
import requests
import json

# Row and Column pins setup
R1 = DigitalOutputDevice(5)
R2 = DigitalOutputDevice(6)
R3 = DigitalOutputDevice(13)
R4 = DigitalOutputDevice(19)

C1 = DigitalInputDevice(12, pull_up=False)
C2 = DigitalInputDevice(16, pull_up=False)
C3 = DigitalInputDevice(20, pull_up=False)
C4 = DigitalInputDevice(21, pull_up=False)

# 허가된 사용자 데이터 (실제로는 데이터베이스나 파일에서 로드해야 함)
AUTHORIZED_USERS = {
    "123456789": {"name": "김철수", "role": "관리자"},
    "234567890": {"name": "이영희", "department": "재배담당"},
    "345678901": {"name": "박지성", "department": "품질관리"}
}

class GreenhouseAccess:
    def __init__(self):
        self.current_input = ""
        self.log_file = "greenhouse_access_log.txt"
    
    def scan_keypad(self, row_pin, characters):
        """키패드의 한 행을 스캔하고 눌린 키를 반환"""
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
    
    def log_access(self, user_id, status):
        """출입 기록을 로그 파일에 저장"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_info = AUTHORIZED_USERS.get(user_id, {"name": "Unknown"})
        log_entry = f"{timestamp} - ID: {user_id} - 이름: {user_info['name']} - 상태: {status}\n"
        
        with open(self.log_file, "a") as f:
            f.write(log_entry)
    
    def verify_user(self):
        """사용자 ID 확인 및 접근 권한 검증"""
        if len(self.current_input) == 9:  # 9자리 입력 완료
            if self.current_input in AUTHORIZED_USERS:
                user = AUTHORIZED_USERS[self.current_input]
                print(f"\n접근 승인!")
                print(f"이름: {user['name']}")
                print(f"부서: {user.get('department', '정보 없음')}")
                print(f"역할: {user.get('role', '일반')}")
                self.log_access(self.current_input, "접근 승인")
            else:
                print("\n접근 거부: 등록되지 않은 사용자")
                self.log_access(self.current_input, "접근 거부")
            
            self.current_input = ""  # 입력 초기화
            print("\n새로운 ID를 입력하세요:")
    
    def run(self):
        """메인 실행 루프"""
        print("온실 출입 관리 시스템")
        print("9자리 ID를 입력하세요:")
        
        try:
            while True:
                key = self.get_pressed_key()
                if key:
                    if key in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        self.current_input += key
                        print("*", end="", flush=True)  # 보안을 위해 * 표시
                    elif key == "#":  # # 키를 누르면 입력 초기화
                        self.current_input = ""
                        print("\n입력이 초기화되었습니다. 다시 입력하세요:")
                    
                    self.verify_user()
                sleep(0.2)  # 디바운싱을 위한 지연
                
        except KeyboardInterrupt:
            print("\n시스템을 종료합니다.")

    def log_access(self, user_id, status):
        """출입 기록을 로그 파일에 저장하고 Django로 전송"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_info = AUTHORIZED_USERS.get(user_id, {"name": "Unknown"})
        log_entry = {
            "timestamp": timestamp,
            "user_id": user_id,
            "name": user_info['name'],
            "status": status
        }

        # 로그 파일 저장
        with open(self.log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")

        # Django 서버로 전송
        try:
            requests.post("http://127.0.0.1/api/keypad_input/", json=log_entry)
        except Exception as e:
            print(f"데이터 전송 실패: {e}")

if __name__ == "__main__":
    access_system = GreenhouseAccess()
    access_system.run()
