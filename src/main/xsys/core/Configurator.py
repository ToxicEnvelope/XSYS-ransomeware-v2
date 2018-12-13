#!/usr/bin/env python
__author__ = "T0x1cEnv31ope"
from src.main.xsys.config.MenuConfig import MenuConfig


class Configurator(MenuConfig, object):
    """
        [Description]
        __init__
        - Construct a Configurator Object
    """
    def __init__(self):
        super(Configurator, self).__init__()

    """
        [Description]
        set_flag
        - This is a property setter         
    """
    @MenuConfig.flag.setter
    def set_flag(self, state):
        self.FLAG = state

    """
        [Description]
        get_flag
        - This is a property getter
    """
    @MenuConfig.flag.getter
    def get_flag(self):
        return self.flag


    """
        [Description]
        get_empty_str
        - This is a property getter
    """
    @MenuConfig.empty_str.getter
    def get_empty_str(self):
        return self.empty_str

    """
        [Description]
        - This is a property getter
    """
    @MenuConfig.win_str.getter
    def get_win(self):
        return self.win_str



    """
        [Description]
        get_lin
        - This is a property getter
    """
    @MenuConfig.lin_str.getter
    def get_lin(self):
        return self.lin_str
