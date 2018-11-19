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
        self.CHUNK_SIZE = 0
        self.SUFFIX = None
        self.SIXTEEN_BYTES = 0
        self.HEX_e = None
        self.HEX_d = None
        self.HEX_r = None
        self.HEX_l = None

    """
        [Description]
        chunk_size
        - This is a property function for CHUNK_SIZE value
    """
    @property
    def chunk_size(self):
        self.CHUNK_SIZE = (65 * 1024)
        return self.CHUNK_SIZE

    """
        [Description]
        get_chunk_size
        - This is a property getter
    """
    @chunk_size.getter
    def get_chunk_size(self):
        return self.chunk_size

    """
        [Description]
        suffix
        - This is a property function for SUFFIX value
    """
    @property
    def suffix(self):
        self.SUFFIX = '.(encrypted)'
        return self.SUFFIX

    """
        [Description]
        get_suffix
        - This is a property getter
    """
    @suffix.getter
    def get_suffix(self):
        return self.suffix

    """
        [Description]
        sixteen_byte
        - This is a property function for SIXTEEN_BYTES value
    """
    @property
    def sixteen_byte(self):
        self.SIXTEEN_BYTES = 16
        return self.SIXTEEN_BYTES

    """
        [Description]
        get_byte_size
        - This is a property getter
    """
    @sixteen_byte.getter
    def get_byte_size(self):
        return self.sixteen_byte

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
