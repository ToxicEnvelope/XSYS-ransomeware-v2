#!/usr/bin/env python
__author__ = "T0x1cEnv31ope"


class MenuConfig(object):

    _CLS = 'cls'
    _CLR = 'clear'
    """
        [Description]
        __init__
        - Construct a MenuConfig Object
    """
    def __init__(self):
        self.FLAG = None
        self.EMPTY_STR = None
        self.WIN = None
        self.LIN = None

    """
        [Description]
        flag
        - This is a property function for FLAG value 
    """
    @property
    def flag(self):
        self.FLAG = True
        return self.FLAG

    """
        [Description]
        set_flag
        - This is a property setter         
    """
    @flag.setter
    def set_flag(self, state):
        self.FLAG = state

    """
        [Description]
        get_flag
        - This is a property getter
    """
    @flag.getter
    def get_flag(self):
        return self.flag

    """
        [Description]
        empty_str
        - This is a property function for EMPTY_STR value
    """
    @property
    def empty_str(self):
        self.EMPTY_STR = ''
        return self.EMPTY_STR

    """
        [Description]
        get_empty_str
        - This is a property getter
    """
    @empty_str.getter
    def get_empty_str(self):
        return self.empty_str

    """
        [Description]
        win_str
        - This is a property function for WIN value
    """
    @property
    def win_str(self):
        self.WIN = 'win'
        return self.WIN

    """
        [Description]
        - This is a property getter
    """
    @win_str.getter
    def get_win(self):
        return self.win_str

    """
        [Description]
        lin_str
        - This is a property function for LIN value
    """
    @property
    def lin_str(self):
        self.LIN = 'lin'
        return self.LIN

    """
        [Description]
        get_lin
        - This is a property getter
    """
    @lin_str.getter
    def get_lin(self):
        return self.lin_str

    """
        [Description]
        clear_console
        - This method will be implemented inside Menu.class
    """
    def clear_console(self):
        pass

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


if __name__ == '__main__':
    assert MenuConfig().get_flag().__eq__(True), \
        'Assert Failed -> FLAG is not {0}'.format(MenuConfig().get_flag())
    assert MenuConfig().get_empty_str().__eq__(''), \
        'Assert Failed -> EMPTY_STR is not {0}'.format(MenuConfig().get_empty_str())
    assert MenuConfig().get_win.__eq__('win'), \
        'Assert Failed -> EMPTY_STR is not {0}'.format(MenuConfig().get_win())
    assert MenuConfig().get_lin().__eq__('lin'), \
        'Assert Failed -> EMPTY_STR is not {0}'.format(MenuConfig().get_lin())
