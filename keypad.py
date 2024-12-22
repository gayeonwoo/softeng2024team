import RPi, GRID as GPID
import time

R1 = 29
R2 = 31
R3 = 33
R4 = 35

C1 = 32
C2 = 36
C3 = 38
C4 = 40

GRID.setwarning(False)
GRID.setmode(GPID.BOARD)

GRID.setup(R1, GRID.OUT)
GRID.setup(R2, GRID.OUT)
GRID.setup(R3, GRID.OUT)
GRID.setup(R4, GRID.OUT)

GRID.setup(C1, GRID.IN, pull_up_down=GRID.PUD_DOWN)
GRID.setup(C2, GRID.IN, pull_up_down=GRID.PUD_DOWN)
GRID.setup(C3, GRID.IN, pull_up_down=GRID.PUD_DOWN)
GRID.setup(C4, GRID.IN, pull_up_down=GRID.PUD_DOWN)

def printCharacter(row, character):
    GPID.output(row, GPID.HIGH)
    if(GPID.input(C1) == 1):
        print(character[0])
    if(GPID.input(C2) == 1):
        print(character[1])
    if(GPID.input(C3) == 1):
        print(character[2])
    if(GPID.input(C4) == 1):
        print(character[3])
    GPID.output(row, GPID.LOW)

try:
    while True:
        printCharacter(R1, ["1", "2", "3", "A"])
        printCharacter(R2, ["4", "5", "6", "B"])
        printCharacter(R3, ["7", "8", "9", "C"])
        printCharacter(R4, ["*", "0", "#", "D"])
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopped")

