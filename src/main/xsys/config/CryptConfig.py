#!/usr/bin/env python
class CryptConfig(object):
    """
        [Description]
        __init__
        - Construct a CryptConfig Object
    """
    def __init__(self):
        self.CHUNK_SIZE = 0
        self.SUFFIX = None
        self.SIXTEEN_BYTES = 0

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


if __name__ == '__main__':
    assert CryptConfig().get_chunk_size.__eq__(66560), \
        'Assert Failed -> CHUNK_SIZE is not {0}'.format(CryptConfig().get_chunk_size)
    assert CryptConfig().get_suffix.__eq__('.(encrypted)'), \
        'Assert failed -> SUFFIX is not {0}'.format(CryptConfig().get_suffix)
    assert CryptConfig().get_byte_size.__eq__(16), \
        'Assert failed -> SIXTEEN_BYTES is not {0}'.format(CryptConfig().get_byte_size)
