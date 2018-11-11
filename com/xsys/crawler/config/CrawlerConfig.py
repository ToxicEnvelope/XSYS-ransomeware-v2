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
