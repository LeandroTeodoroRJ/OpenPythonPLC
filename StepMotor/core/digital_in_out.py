'''
 * Description: It implements digital pins to input and output
 * Stable: Yes
 * Version: 1.1.0
 * Last Uptate: 02.07.26
 * Dependences:
 *      --ArduinoInterface V1.0.0
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

from HardwareResources.ArduinoInterface import DigitalCard

class DigitalPin:
    def __init__(self):
        self.state = 0

    def get_state(self):
        return self.state

    def update(self):
        pass

class DigitalInput(DigitalPin):
    def update(self, dg_card, pin):
        self.input, self.output = dg_card.get_status()
        if (DigitalCard.bit_is_active(self.input, pin) == True):
            self.state = 1
        else:
            self.state = 0

class Coil(DigitalPin):
    def set_state(self, value):
        self.state = value

    def update(self, dg_card, pin):
        if (self.state == True):
            dg_card.set_output_status(1, pin)
        else:
            dg_card.set_output_status(0, pin)


class InputPulseUp(DigitalInput):
    def __init__(self):
        super().__init__()
        self.pressed = 0
        self.activated = 0
        self.executed = 0

    def update(self, dg_card, pin):
        self.input, self.output = dg_card.get_status()
        if (DigitalCard.bit_is_active(self.input, pin) == True):
            self.state = 1
            if (self.pressed == 0 and self.executed == 0):
                self.activated = 1
                self.executed = 1
                self.pressed = 1
        else:
            self.state = 0
            self.activated = 0
            self.pressed = 0

    def action(self):
        if (self.activated == 1 and self.executed == 1):
            return 1
        else:
            return 0

    def finished_action(self):
        self.executed = 0


class InputPulseDown(DigitalInput):
    def __init__(self):
        super().__init__()
        self.pressed = 0
        self.activated = 0
        self.executed = 0

    def update(self, dg_card, pin):
        self.input, self.output = dg_card.get_status()
        if (DigitalCard.bit_is_active(self.input, pin) == True):
            self.state = 1
            self.state = 0
            self.activated = 0
            self.pressed = 0
        else:
            if (self.pressed == 0 and self.executed == 0):
                self.activated = 1
                self.executed = 1
                self.pressed = 1

    def action(self):
        if (self.activated == 1 and self.executed == 1):
            return 1
        else:
            return 0

    def finished_action(self):
        self.executed = 0
