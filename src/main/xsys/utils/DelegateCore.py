#!/usr/bin/env python
import uuid, random, string
from src.main.xsys.core.SuperBase import SuperBase
from src.main.xsys.cryptography.CryptoManager import CryptoManager


class DelegateCore(SuperBase, CryptoManager):
    """
        [Description]
        __init__
        - Construct a SuperBase Object
    """
    def __init__(self):
        super(DelegateCore, self).__init__()
        self._hashkey = None

    """
        [Description]
        generate_hashed_key
        - Generate a 16-byte key from a phrase
        :param -> phrase:str - a key to be hashed
        :return - a string uuid5 pra-phrase
    """
    def generate_hash_key(self, phrase=None):
        if phrase is None:
            return uuid.uuid5(uuid.NAMESPACE_X500, self.randomize()).__str__()
        else:
            return uuid.uuid5(uuid.NAMESPACE_X500, phrase).__str__()

    """
        [Description]
        randomize
        - Generate a random string with size of 16-bytes
    """
    def randomize(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(self.get_byte_size))

    @property
    def hashkey(self):
        return self._hashkey

    @hashkey.getter
    def get_hash_key(self):
        return self.hashkey

    @hashkey.setter
    def set_hash_key(self, key):
        self._hashkey = self.generate_hash_key(key)
