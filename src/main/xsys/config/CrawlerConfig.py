#!/usr/bin/env python
__author__ = "T0x1cEnv31ope"


class CrawlerConfig(object):
    """
        [Description]
        __init__
        - Construct a CrawlerConfig Object
    """
    def __init__(self):
        super(CrawlerConfig, self).__init__()
        self.HEX_e = None
        self.HEX_d = None
        self.HEX_r = None
        self.HEX_l = None

    """
        [Description]
        hex_e
        - This is a property function for HEX_e value
    """
    @property
    def hex_e(self):
        self.HEX_e = '0x65'
        return self.HEX_e

    """
        [Description]
        get_hex_e
        - This is a property getter
    """
    @hex_e.getter
    def get_hex_e(self):
        return self.hex_e

    """
        [Description]
        hex_d
        - This is a property function for HEX_d value
    """
    @property
    def hex_d(self):
        self.HEX_d = '0x64'
        return self.HEX_d

    """
        [Description]
        get_hex_d
        - This is a property getter
    """
    @hex_d.getter
    def get_hex_d(self):
        return self.hex_d

    """
        [Description]
        hex_r
        - This is a property function for HEX_r value
    """
    @property
    def hex_r(self):
        self.HEX_r = '0x72'
        return self.HEX_r

    """
        [Description]
        get_hex_r
        - This is a property getter
    """
    @hex_r.getter
    def get_hex_r(self):
        return self.hex_r

    """
        [Description]
        hex_l
        - This is a property function for HEX_l value
    """
    @property
    def hex_l(self):
        self.HEX_l = '0x6c'
        return self.HEX_l

    """
        [Description]
        get_hex_l
        - This is a property getter
    """
    @hex_l.getter
    def get_hex_l(self):
        return self.hex_l

    """
        [Description]
        linear_file_crawler
        - This method will be implemented inside Crawler.class
    """
    @staticmethod
    def linear_file_crawler():
        pass


if __name__ == '__main__':
    assert CrawlerConfig().get_hex_e.__eq__(hex(ord('e'))), \
        'Assert failed -> HEX_e is not {0}'.format(CrawlerConfig().get_hex_e)
    assert CrawlerConfig().get_hex_d.__eq__(hex(ord('d'))), \
        'Assert failed -> HEX_d is not {0}'.format(CrawlerConfig().get_hex_d)
    assert CrawlerConfig().get_hex_r.__eq__(hex(ord('r'))), \
        'Assert failed -> HEX_r is not {0}'.format(CrawlerConfig().get_hex_r)
    assert CrawlerConfig().get_hex_l.__eq__(hex(ord('l'))), \
        'Assert failed -> HEX_l is not {0}'.format(CrawlerConfig().get_hex_l)
