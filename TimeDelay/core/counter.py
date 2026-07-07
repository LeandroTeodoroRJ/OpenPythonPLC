'''
 * Description: It implements PLC counters
 * Stable: Yes
 * Version: 1.0.0
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

class Counter:
    def __init__(self):
        self.counter = 0

    def set_counter(self, new_value):
        self.counter = new_value

    def reset_counter(self):
        self.counter = 0

    def get_counter(self):
        return self.counter

    def is_over(self):
        pass

    def step(self):
        pass


class CounterUp(Counter):
    def __init__(self):
        super().__init__()
        self.target = 0

    def step(self):
        self.counter = self.counter + 1

    def set_target(self, value):
        self.target = value

    def is_over(self):
        if (self.counter == self.target):
            return 1
        else:
            return 0

class CounterDown(Counter):
    def step(self):
        self.counter = self.counter - 1

    def is_over(self):
        if (self.counter == 0):
            return 1
        else:
            return 0
