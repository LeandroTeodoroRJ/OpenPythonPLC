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

class DigitalCard:
    def __init__(self, serial_comm):
        self.input_status = 0
        self.output_status = 0
        self.ser = serial_comm
        time.sleep(0.1)

    def get_status(self):
        return self.input_status, self.output_status

    def serial_loop_update(self):
        self.receiver = self.ser.readlines()
#        print(type(self.receiver))
#        print(self.receiver)
        if self.receiver != []:
            #Cast to String
            self.str_buffer_receiver = self.receiver[0].decode("utf-8")
            partial1 = self.str_buffer_receiver[0:2]
            partial2 = self.str_buffer_receiver[2:4]
            self.input_status = int(partial1)
            self.output_status = int(partial2)
            self.ser.write(b'23')
            time.sleep(0.01)
        else:
            #TODO: Implement usart fail receiver log
            print("READ USART FAIL")


    def send_message(self, cmd):
        self.out = bytes(cmd, "utf-8")
        self.ser.write(self.out)


    @staticmethod
    def bit_is_active(byte_name, bit_number):
        if (byte_name & (1 << bit_number) != 0):
            return True
        else:
            return False



#Test Class Start
import serial
import time
import os

time.sleep(0.4)

#Dissable DTR line to not reset arduino
os.system("stty -F /dev/ttyUSB0 -hupcl")
time.sleep(1)

ser = serial.Serial('/dev/ttyUSB0',
115200,
timeout=0.05,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS
)

dg_card1 = DigitalCard(ser)

#Concatenate string dataframe
param1 = 0x24
param2 = 0x09
msg = f"{param1: 03X}" + f"{param2: 03X}"
msg = msg.replace(" ", "")

print("Str message to send: " + msg)

dg_card1.send_message(msg)

#Delay between tramitter-receiver mode
time.sleep(1)	#Be carefull with to fast time delay

#Read input and outputs status

msg = "23"
dg_card1.send_message(msg)

time.sleep(0.03)
while True:
    dg_card1.serial_loop_update()
    input_info, output_info = dg_card1.get_status()
    print("Input Info:")
    print(input_info)
    print("Output Info:")
    print(output_info)
    if (DigitalCard.bit_is_active(input_info, 0) == True):
        print("Button Pressed")
    else:
        print("Button Not Pressed")

ser.close()


