#!/usr/bin/env python
__author__ = "T0x1cEnv31ope"
import os
from src.main.xsys.core.XSYS import XSYS
from src.main.xsys.core.Configurator import Configurator


class Menu(Configurator, XSYS):
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
        while self.FLAG:
            main_choice = input('\n[?] Which operation would you like to do...? \
                                   \n\tD -> Decrypt \
                                   \n\tE -> Encrypt\n[$] ')
            if len(main_choice) > 1:
                main_choice = main_choice[:len(main_choice)-len(main_choice)+1]
            hex_m_choice = hex(ord(main_choice.lower()))
            # hex(dec("e")) = 0x65
            if hex_m_choice.__eq__(self.HEX_e):
                self.clear_console()
                self.input_handler()
            # hex(dec("d")) = 0x64
            elif hex_m_choice.__eq__(self.HEX_d):
                self.clear_console()
                self.input_handler()
            else:
                print('[!] "{0}" is not supported choice..!'.format(hex_m_choice))
                self.clear_console()
                continue

    """
        [Description]
        input_handler
        - This method responsible to
        handle the input received by the user.
    """
    def input_handler(self):
        enc_choice = input('\n[?] Which search operation would you prefer? \
                                              \n\tR -> Recursive \
                                              \n\tL -> Linear\n[$] ')
        if len(enc_choice) > 1:
            enc_choice = enc_choice[:len(enc_choice) - len(enc_choice) + 1]
        hex_e_choice = hex(ord(enc_choice.lower()))
        # hex(dec("r")) = 0x72
        if hex_e_choice.__eq__(self.HEX_r):
            print('\n[+] Current Location: {0}'.format(os.getcwd()))
            nav_choice = input('[>>] Move to a Root Dir for scan starting point\n[-] ')
            if nav_choice.__eq__(self.EMPTY_STR) or len(nav_choice) <= 2:
                print('[!] Cannot use this `{0}` as path, must be at least 3 chars'.format(nav_choice))
                nav_choice = input('[>>] Move to a Root Dir for scan starting point\n[-] ')
            os.chdir(nav_choice)
            print('Actual Location: {0}'.format(os.getcwd()))
            rtar_files = self.recursive_file_crawler()
            cntr = 0
            for file in rtar_files:
                cntr += 1
                print('[{0}] {1}'.format(cntr, file))
        # hex(dec("l")) = 0x6c
        elif hex_e_choice.__eq__(self.HEX_l):
            print('\n[+] Current Location: {0}'.format(os.getcwd()))
            nav_choice = input('[>>] Move to a Root Dir for scan starting point\n[-] ')
            if nav_choice.__eq__(self.EMPTY_STR) or len(nav_choice) <= 2:
                print('[!] Cannot use this `{0}` as path, must be at least 3 chars'.format(nav_choice))
                nav_choice = input('[>>] Move to a Root Dir for scan starting point\n[-] ')
            os.chdir(nav_choice)
            print('Actual Location: {0}'.format(os.getcwd()))
            ltar_files, res = self.linear_file_crawler()
            cntr = 0
            for file in ltar_files:
                cntr += 1
                print('[{0}] {1}'.format(cntr, file))
            print('{0}'.format(res))
        else:
            print('[!] "{0}" is not supported choice..!'.format(hex_e_choice))
            self.clear_console()

    """
        [Description]
        show_first_menu
        - Print some lines to the console
    """
    @staticmethod
    def show_first_menu():
        a1 = "\n\t\t################################"
        a2 = "\n\t\t## ~~~~~~~~ XSYS 2.0 ~~~~~~~~ ##"
        a3 = "\n\t\t##   Encrypt   ||   Decrypt   ##"
        a4 = "\n\t\t## ~~~~~~~~~~~~~~~~~~~~~~~~~~ ##"
        a5 = "\n\t\t## .....M.a.d.e....B.y....... ##"
        a6 = "\n\t\t##    Yahav   N   Hoffman     ##"
        a7 = "\n\t\t##          a.k.a.            ##"
        a8 = "\n\t\t## T 0 x 1 c  E n v 3 1 o p e ##"
        a9 = "\n\t\t################################"
        a0 = '{0}{1}{2}{3}{4}{5}{6}{7}{8}\n\n'.format(a1, a2, a3, a4, a5, a6, a7, a8, a9)
        x1 = " Attention !!\n"
        x2 = " This program may cause harm to your computer files system, machine functionality,\n"
        x3 = " personal data and private information.\n"
        x4 = " XSYS is a tool that build an Hierarchical Tree diagram of\n"
        x5 = " all files from your root folder and its descendants until its (E)ncrypt || (D)ecrypt any leaf\n"
        x6 = " in the system tree diagram.\n"
        print('{0}{1}{2}{3}{4}{5}{6}'.format(a0, x1, x2, x3, x4, x5, x6))

    """
        [Description]
        choice_menu
        - Print some lines to the console
    """
    @staticmethod
    def choice_menu():
        a1 = "[!] You can send the encryption key to your personal email\n"
        a2 = "    via our TorSMTP configuration."
        print('{0}{1}'.format(a1, a2))


if __name__ == "__main__":
    menu = Menu()
    menu.init()
