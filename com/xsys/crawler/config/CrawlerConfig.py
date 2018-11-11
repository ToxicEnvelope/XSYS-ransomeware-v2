#!/usr/bin/env python


class CrawlerConfig(object):
    def __init__(self):
        self.CHUNK_SIZE = (65 * 1024)
        self.SUFFIX = '.(encrypted)'
        self.SIXTEEN_BYTES = 16
        self.HEX_e = '0x65'
        self.HEX_d = '0x64'
        self.HEX_r = '0x72'
        self.HEX_l = '0x6c'


if __name__ == '__main__':
    conf = CrawlerConfig()
    assert conf.CHUNK_SIZE.__eq__(65*1024), 'Assert Failed -> CHUNK_SIZE is not {0}'.format(conf.CHUNK_SIZE)
    assert conf.SUFFIX.__eq__('.(encrypted)'), 'Assert failed -> SUFFIX is not {0}'.format(conf.SUFFIX)
    assert conf.HEX_e.__eq__(hex(ord('e'))), 'Assert failed -> HEX_e is not {0}'.format(conf.HEX_e)
    assert conf.HEX_d.__eq__(hex(ord('d'))), 'Assert failed -> HEX_d is not {0}'.format(conf.HEX_d)
    assert conf.HEX_r.__eq__(hex(ord('r'))), 'Assert failed -> HEX_r is not {0}'.format(conf.HEX_r)
    assert conf.HEX_l.__eq__(hex(ord('l'))), 'Assert failed -> HEX_l is not {0}'.format(conf.HEX_l)
