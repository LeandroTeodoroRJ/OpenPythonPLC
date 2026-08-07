'''
 * Description: How to use a step motor
 * Stable: Yes
 * Version: 1.0.0
 * Last Uptate: 07.08.26
 * Dependences:
 *  -- motor v1.0.0
 *  -- pySerial
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
from core.motor import StepMotor
import time
import os

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
smotor = StepMotor(dg_card1)

while True:
    smotor.update_position(100)
    time.sleep(0.5)
    smotor.update_position(100)
    time.sleep(0.5)
    smotor.update_position(100)
    time.sleep(0.5)
    smotor.update_position(100)
    time.sleep(0.5)
    smotor.update_position(-400)
    time.sleep(2)
#    time.sleep(0.50)  # scan time - disable global scan time
