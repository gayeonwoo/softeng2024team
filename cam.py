from picamera import PiCamera       //파이카메라 라이브러리에서 PiCamera 클래스를 불러옵니다.
from time import sleep             // 시간지연 함수를 불러옵니다

camera = PiCamera()                // camera라는 객체를 만듭니다.

camera.start_preview()             // 카메라 미리보기를 실행합니다.
sleep(5)                            // 5초간 대기합니다.
camera.capture('/home/pi/test.jpg')            //카메라를 사용해서 사진을 찍습니다.
camera.stop_preview()              // 카메라 미리보기를 정지합니다.
# [출처] 파이썬으로 라즈베리파이 카메라모듈 제어하기|작성자 황제곰