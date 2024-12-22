import RPi.GPIO as GPIO
import time

R1 = 29
R2 = 31
R3 = 33
R4 = 35

C1 = 32
C2 = 36
C3 = 38
C4 = 40

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(R3, GPIO.OUT)
GPIO.setup(R4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def printCharacter(row, character):
    GPIO.output(row, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        print(character[0])
    if(GPIO.input(C2) == 1):
        print(character[1])
    if(GPIO.input(C3) == 1):
        print(character[2])
    if(GPIO.input(C4) == 1):
        print(character[3])
    GPIO.output(row, GPIO.LOW)

try:
    while True:
        printCharacter(R1, ["1", "2", "3", "A"])
        printCharacter(R2, ["4", "5", "6", "B"])
        printCharacter(R3, ["7", "8", "9", "C"])
        printCharacter(R4, ["*", "0", "#", "D"])
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopped")

