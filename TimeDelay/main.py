'''
 * Description: Button and delay
 * Stable: Yes
 * Version: 1.0.0
 * Last Uptate: 03.07.26
 * Dependences:
 *  -- digital_in_out v1.0.0
 *  -- ArduinoInterface
 *  -- DelayPLC
 * Current: Yes
 * Maintainer: leandroteodoro.engenharia@gmail.com
 * Architecture: RaspberryPi Model 3 B+
 * Compile/Interpreter: python3 v3.10.12
 * Programer: No
 * Operational System: Raspbian GNU V10
 * Access: Public
 * Changelog: No
 * Readme and
 * Documents: No
 * Links:
 * Comments:
 *
'''

from HardwareResources.ArduinoInterface import *
import serial
from core.digital_in_out import DigitalInput, InputPulseUp, Coil
from core.time_delay import DelayPLC
import time
import os

time.sleep(WAKEUP_DELAY)

#Dissable DTR line to not reset arduino
os.system("stty -F /dev/ttyUSB0 -hupcl")
time.sleep(BOOT_DELAY)

ser = serial.Serial('/dev/ttyUSB0',
115200,
timeout=SERIAL_TIMEOUT,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS
)

dg_card1 = DigitalCard(ser)

X1 = DigitalInput()
Y1 = Coil()
DL1 = DelayPLC(4)

def delay_finished():
    Y1.set_state(1)
    Y1.update(dg_card1, 0)
    DL1.reset()

while True:
    print("Program is Running")
    dg_card1.serial_loop_update()
    X1.update(dg_card1, 0)
    if (X1.get_state() == 1):
        DL1.start()
    if (DL1.is_end() == 1):
        delay_finished()
        print("END DELAY")
    else:
        print("Delay not end.")
    time.sleep(0.5)  # scan time - global scan time

