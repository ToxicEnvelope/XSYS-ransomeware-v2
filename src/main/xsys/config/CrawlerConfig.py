#!/usr/bin/env python
__author__ = "T0x1cEnv31ope"
from src.main.xsys.config.MenuConfig import MenuConfig


class CrawlerConfig(MenuConfig, object):
    """
        [Description]
        __init__
        - Construct a CrawlerConfig Object
    """
    def __init__(self):
        super(CrawlerConfig, self).__init__()
        self.CHUNK_SIZE = (65 * 1024)
        self.SUFFIX = '.(encrypted)'
        self.SIXTEEN_BYTES = 16
        self.HEX_e = '0x65'
        self.HEX_d = '0x64'
        self.HEX_r = '0x72'
        self.HEX_l = '0x6c'


if __name__ == '__main__':
    assert CrawlerConfig().CHUNK_SIZE.__eq__(66560), \
        'Assert Failed -> CHUNK_SIZE is not {0}'.format(CrawlerConfig().CHUNK_SIZE)
    assert CrawlerConfig().SUFFIX.__eq__('.(encrypted)'), \
        'Assert failed -> SUFFIX is not {0}'.format(CrawlerConfig().SUFFIX)
    assert CrawlerConfig().HEX_e.__eq__(hex(ord('e'))), \
        'Assert failed -> HEX_e is not {0}'.format(CrawlerConfig().HEX_e)
    assert CrawlerConfig().HEX_d.__eq__(hex(ord('d'))), \
        'Assert failed -> HEX_d is not {0}'.format(CrawlerConfig().HEX_d)
    assert CrawlerConfig().HEX_r.__eq__(hex(ord('r'))), \
        'Assert failed -> HEX_r is not {0}'.format(CrawlerConfig().HEX_r)
    assert CrawlerConfig().HEX_l.__eq__(hex(ord('l'))), \
        'Assert failed -> HEX_l is not {0}'.format(CrawlerConfig().HEX_l)
