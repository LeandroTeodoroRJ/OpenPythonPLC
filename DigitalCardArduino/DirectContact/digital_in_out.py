'''
 * Description: It implements digital pins to input and output
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
 *
'''

from x64interface import X64Interface

class DigitalPin:
    def __init__(self):
        self.state = 0;

    def get_state(self):
        return self.state

    def update(self):
        pass

class DigitalInput(DigitalPin):
    def update(self, file_path):
        self.file = X64Interface()
        self.file.set_path(file_path)
        self.state, self.error = self.file.read_bol()

class Coil(DigitalPin):
    def set_state(self, value):
        self.state = value

    def update(self, file_path):
        self.file = X64Interface()
        self.file.set_path(file_path)
        self.error = self.file.write_bol(self.state)
