'''
 * Description: PLC delay with parallel process
 * Stable: Yes
 * Version: 1.0.0
 * Last Uptate: 05.07.26
 * Dependences:
 *      -- _thread module
 * Current: Yes
 * Maintainer: leandroteodoro.engenharia@gmail.com
 * Architecture: X64
 * Compile/Interpreter: python3 v3.7.3
 * Programer: No
 * Operational System: Raspbian
 * Access: Public
 * Changelog: No
 * Readme and
 * Documents: No
 * Links:
 * Comments:
 *
'''

import _thread
import time

class DelayPLC:
    def __init__(self, delay_second):
        self.time = delay_second
        self.end = 0
        self.blocked = 0

    def is_end(self):
        return self.end

    def delay_time(self):
        time.sleep(self.time)
        self.end = 1
        self.blocked = 0

    def start(self):
        if (self.blocked == 0):
            self.end = 0
            self.blocked = 1
            _thread.start_new_thread(self.delay_time, ())

    def reset(self):
        self.end = 0

