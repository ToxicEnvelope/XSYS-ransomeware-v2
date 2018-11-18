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
        - This method will be implemented inside Menu.class
    """
    @staticmethod
    def show_first_menu():
        pass

    """
        [Description]
        choice_menu
        - This method will be implemented inside Menu.class
    """
    @staticmethod
    def choice_menu():
        pass


if __name__ == '__main__':
    assert MenuConfig().get_flag().__eq__(True), \
        'Assert Failed -> FLAG is not {0}'.format(MenuConfig().get_flag())
    assert MenuConfig().get_empty_str().__eq__(''), \
        'Assert Failed -> EMPTY_STR is not {0}'.format(MenuConfig().get_empty_str())
    assert MenuConfig().get_win.__eq__('win'), \
        'Assert Failed -> EMPTY_STR is not {0}'.format(MenuConfig().get_win())
    assert MenuConfig().get_lin().__eq__('lin'), \
        'Assert Failed -> EMPTY_STR is not {0}'.format(MenuConfig().get_lin())
