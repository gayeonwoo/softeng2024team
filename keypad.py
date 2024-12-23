from gpiozero import DigitalOutputDevice, DigitalInputDevice
from time import sleep

# Row pins as outputs
R1 = DigitalOutputDevice(29)
R2 = DigitalOutputDevice(31)
R3 = DigitalOutputDevice(33)
R4 = DigitalOutputDevice(35)

# Column pins as inputs with pull-down resistors
C1 = DigitalInputDevice(32, pull_up=False)
C2 = DigitalInputDevice(36, pull_up=False)
C3 = DigitalInputDevice(38, pull_up=False)
C4 = DigitalInputDevice(40, pull_up=False)

def print_character(row_pin, characters):
    """
    Scans one row of the keypad and prints the corresponding character if a button is pressed
    """
    row_pin.on()  # Set row high
    
    # Check each column
    if C1.value:
        print(characters[0])
    if C2.value:
        print(characters[1])
    if C3.value:
        print(characters[2])
    if C4.value:
        print(characters[3])
        
    row_pin.off()  # Set row low

try:
    while True:
        # Scan each row
        print_character(R1, ["1", "2", "3", "A"])
        print_character(R2, ["4", "5", "6", "B"])
        print_character(R3, ["7", "8", "9", "C"])
        print_character(R4, ["*", "0", "#", "D"])
        sleep(0.1)
        
except KeyboardInterrupt:
    print("Stopped")
    # GPIO Zero automatically cleans up pins on program exit
