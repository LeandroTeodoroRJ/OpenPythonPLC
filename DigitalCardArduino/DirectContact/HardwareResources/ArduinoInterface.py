'''
 * Description: It implements serial communication with Arduino Digital Card
 * Stable: Yes
 * Version: 1.0.0
 * Last Uptate: 21.06.26
 * Dependences:
 *
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
 *  -- Use Arduino Firmware V1.1.0: 
 *     https://github.com/LeandroTeodoroRJ/BareMetalLowCost_Arduino/tree/main/Serial_TTY
 *
'''

import time


#General Definitions
WAKEUP_DELAY = 0.4
BOOT_DELAY = 1
DELAY_BETWEEN_COMMANDS = 0.1
DELAY_BEFORE_READ = 0.01


class DigitalCard:
    def __init__(self, serial_comm):
        self.input_status = 0x00
        self.output_status = 0x00
        self.ser = serial_comm
#        time.sleep(0.1)

    def get_status(self):
        return self.input_status, self.output_status

    def serial_loop_update(self):
        #Updatde Output
        self.msg = "24"
        self.msg = self.msg + f"{self.output_status: 03X}"
        self.msg = self.msg.replace(" ", "")
        self.msg = bytes(self.msg, "utf-8")
        self.ser.write(self.msg)
        time.sleep(DELAY_BETWEEN_COMMANDS)	#Be carefull with to fast time delay
        #Update status
        self.ser.write(b'23')
        time.sleep(DELAY_BEFORE_READ)
        self.receiver = self.ser.readlines()
#        print(type(self.receiver))
#        print(self.receiver)
        if self.receiver != []:
            #Cast to String
            self.str_buffer_receiver = self.receiver[0].decode("utf-8")
            partial1 = self.str_buffer_receiver[0:2]
            partial2 = self.str_buffer_receiver[2:4]
            self.input_status = int(partial1)
            #TODO: Analize if is important create a feedback 
            #output loop error monitoring.
#           self.error_output_status = int(partial2)
        else:
            #TODO: Implement usart fail receiver log
            print("READ USART FAIL")

    def send_message(self, cmd):
        self.out = bytes(cmd, "utf-8")
        self.ser.write(self.out)

    def set_output_status(self, level, bit_number):
        if (level == 1):
            self.output_status = self.output_status | (1 << bit_number)
        else:
            self.mask = ~(1 << bit_number)
            self.output_status = self.output_status & self.mask

    @staticmethod
    def bit_is_active(byte_name, bit_number):
        if (byte_name & (1 << bit_number) != 0):
            return True
        else:
            return False


'''
#Test Class Start
import serial
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

#Read input and outputs status
time.sleep(DELAY_BEFORE_READ)
while True:
    dg_card1.serial_loop_update()
    input_info, output_info = dg_card1.get_status()
    print("Input Info:")
    print(input_info)
    print("Output Info:")
    print(output_info)
    if (DigitalCard.bit_is_active(input_info, 0) == True):
        print("Button Pressed")
        dg_card1.set_output_status(True, 0)
    else:
        print("Button Not Pressed")
        dg_card1.set_output_status(False, 0)


ser.close()
'''

