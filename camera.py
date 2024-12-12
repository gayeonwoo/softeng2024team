import cv2

# 카메라 초기화
cap = cv2.VideoCapture(0)

while True:
  # 카메라로부터 프레임 읽기
  ret, frame = cap.read()
         
  if not ret:
    print("카메라를 열 수 없습니다.")
    break
         
  # 프레임을 윈도우에 표시
  cv2.imshow('Camera', frame)

  # 'q' 키를 누르면 종료
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
