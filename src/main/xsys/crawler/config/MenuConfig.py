#!/usr/bin/env python


class MenuConfig(object):
    """
        [Description]
        __init__
        - Construct a MenuConfig Object
    """
    def __init__(self):
        self.FLAG = True
        self.EMPTY_STR = ''


if __name__ == '__main__':
    assert MenuConfig().FLAG.__eq__(True), \
        'Assert Failed -> FLAG is not {0}'.format(MenuConfig().FLAG)
    assert MenuConfig().FLAG.__eq__(''), \
        'Assert Failed -> EMPTY_STR is not {0}'.format(MenuConfig().EMPTY_STR)
