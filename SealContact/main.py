'''
 * Description: It implements seal contact PLC example using python
 * Stable: Yes
 * Version: 1.0.0
 * Last Uptate: 21.06.26
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

from digital_in_out import DigitalInput, Coil
from time import sleep

X1 = DigitalInput()     #button ON
X2 = DigitalInput()     #button OFF
Y1 = Coil()

def seal_contact():
    if X1.get_state() == 1:
        Y1.set_state(1)
        Y1.update(r'./Y1.output')
        return

    if X2.get_state() == 1:
        Y1.set_state(0)
        Y1.update(r'./Y1.output')

while True:
    X1.update(r'./X1.input')
    X2.update(r'./X2.input')
    seal_contact()
    sleep(0.03)  # scan time
