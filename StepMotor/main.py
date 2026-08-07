'''
 * Description: How to use industrial encoder
 * Stable: Yes
 * Version: 1.0.1
 * Last Uptate: 03.07.26
 * Dependences:
 *  -- digital_in_out v1.0.0
 *  -- x64interface v1.0.0
 * Current: Yes
 * Maintainer: leandroteodoro.engenharia@gmail.com
 * Architecture: RaspberryPi Model 3 B+
 * Compile/Interpreter: python3 v3.7
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
from core.encoder import RotaryEncoder as re
from core.motor import StepMotor
import time
import os
import _thread

CARD_TIME_UPDATE = 0.1

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
#encoder = re(dg_card1)
smotor = StepMotor(dg_card1)

'''
def card_update():
    while True:
        time.sleep(CARD_TIME_UPDATE)
        dg_card1.serial_loop_update()
        dg_card1.encoder_update()

#Start thread to communication card update request
_thread.start_new_thread(card_update, ())
'''

while True:
#    encoder.update()
#    print(encoder.get_position())
    smotor.update_position(400)
    time.sleep(2)
    smotor.update_position(-200)
    time.sleep(2)
#    time.sleep(0.50)  # scan time - disable global scan time
