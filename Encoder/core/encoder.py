'''
 * Description: It implements encoder drive
 * Stable: Yes
 * Version: 1.0.0
 * Last Uptate: 23.07.26
 * Dependences:
 *      -- ArduinoInterface v1.1.0
 * Current: Yes
 * Maintainer: leandroteodoro.engenharia@gmail.com
 * Architecture: RaspberryPi 3 B+
 * Compile/Interpreter: python3 v3.7
 * Programer: No
 * Operational System: Raspbian v10
 * Access: Public
 * Changelog: No
 * Readme and
 * Documents: No
 * Links:
 * Comments:
 *
'''

class RotaryEncoder:
    def __init__(self, card):
        self.digi_card = card
        self.count = 0
        self.absolute_position = 0

    def update(self):
        self.count = self.digi_card.get_encoder_value()
        self.absolute_position = self.count - 32000

    def get_position(self):
        return self.absolute_position
