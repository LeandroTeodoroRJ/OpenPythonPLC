'''
 * Description: It implements motors drives
 * Stable: Yes
 * Version: 1.0.0
 * Last Uptate: 07.08.26
 * Dependences:
 *      -- ArduinoInterface v1.2.0
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


class StepMotor:
    """
    This class implement step motor using Arduino nano as
    expand digital card and using DM556 Step Driver.
    Check Serial_TTY Arduino correct version on ArduinoInterface
    documentation.
    """
    def __init__(self, card):
        self.digi_card = card
        self.position = 0

    def update_position(self, value):
        self.position = value
        self.digi_card.set_step_motor_position(self.position)
