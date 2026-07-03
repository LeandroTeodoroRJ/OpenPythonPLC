'''
 * Description: It implements input pulse button test
 * Stable: Yes
 * Version: 1.0.0
 * Last Uptate: 03.07.26
 * Dependences:
 *  -- digital_in_out v1.0.0
 *  -- x64interface v1.0.0
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
from core.digital_in_out import InputPulseUp, Coil
from core.counter import CounterUp, CounterDown
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

X1 = InputPulseUp()
Y1 = Coil()
C1 = CounterUp()
C1.set_target(10)

def implement_action():
    C1.step()
    X1.finished_action()

def counter_finished():
    Y1.set_state(1)
    Y1.update(dg_card1, 0)

while True:
    dg_card1.serial_loop_update()
    X1.update(dg_card1, 0)
    if (X1.action() == 1):
        implement_action()
    if (C1.is_over() == 1):
        counter_finished()
#    time.sleep(0.03)  # scan time - disable global scan time
