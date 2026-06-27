import serial
import time
import os

#Dissable DTR line to not reset arduino
os.system("stty -F /dev/ttyUSB0 -hupcl")

ser = serial.Serial('/dev/ttyUSB0',
115200,
timeout=1,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS
)

time.sleep(0.1)

#Concatenate string dataframe
param1 = 0x24
param2 = 0x09
msg = f"{param1: 03X}" + f"{param2: 03X}"
msg = msg.replace(" ", "")
out = bytes(msg, "utf-8")
print("Out message")
print(out)

#Leds turn on test
ser.write(out)
#to turn off leds #echo -ne 2400 > /dev/ttyUSB0

#Delay between tramitter-receiver mode
time.sleep(1)	#Be carefull with to fast time delay

#Read input and outputs status
ser.write(b'23')
time.sleep(0.03)
receiver = ser.readlines()
print(type(receiver))
print(receiver)

#Cast to String
print("Cast to String")
str_buffer_receiver = receiver[1].decode("utf-8")
print(type(str_buffer_receiver))
print(str_buffer_receiver)

ser.close()

