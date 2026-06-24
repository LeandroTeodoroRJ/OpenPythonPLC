'''
 * Description: PC interface to use files as interface to simulate
 *      input and output pins.
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
 *
'''

'''
Implement file bool value read and write file to x64 architecture
'''
class X64Interface:
    def __init__(self):
        self.file_name = r''

    def set_path(self, path):
        self.file_name = path

    '''
    Read a boolean value into file, return 0 if the read operation successful
    Error Codes:
    0 - No error_code
    1 - No boolean value
    2 - Empty file or not integer number
    3 - File not found
    '''
    def read_bol(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                self.text = file.read()
                self.value = int(self.text[0])
                if self.value == 0 or self.value == 1:
                    return self.value, 0
                else:
                    return 0, 1
        except (ValueError, IndexError):
            return 0, 2
        except FileNotFoundError:
            return 0, 3


    '''
    Write a boolean value into file
    '''
    def write_bol(self, value):
        with open(self.file_name, "w", encoding="utf-8") as file:
            if value == 0 or value == 1:
                file.write(str(value))
                return 0
            else:
                return 1
