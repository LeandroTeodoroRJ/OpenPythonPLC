'''
 * Description: It implements direct line contact with PLC example
 * Stable: Yes
 * Version: 1.0.0
 * Last Uptate: 28.06.26
 * Dependences:
 *  -- digital_in_out v1.0.0
 *  -- x64interface v1.0.0
 * Current: Yes
 * Maintainer: leandroteodoro.engenharia@gmail.com
 * Architecture: X64
 * Compile/Interpreter: python3 v3.10.12
 * Programer: No
 * Operational System: Ubuntu Mint 22.04
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
from digital_in_out import DigitalInput, Coil
import time
import os

time.sleep(WAKEUP_DELAY)

#Dissable DTR line to not reset arduino
os.system("stty -F /dev/ttyUSB0 -hupcl")
time.sleep(BOOT_DELAY)

ser = serial.Serial('/dev/ttyUSB0',
115200,
timeout=0.05,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS
)

dg_card1 = DigitalCard(ser)

X1 = DigitalInput()     #button ON
Y1 = Coil()

def direct_contact():
    if X1.get_state() == 1:
        Y1.set_state(1)
    else:
        Y1.set_state(0)
    Y1.update(dg_card1, 0)

while True:
    dg_card1.serial_loop_update()
    X1.update(dg_card1, 0)
    direct_contact()
    time.sleep(0.03)  # scan time
