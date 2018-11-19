#!/usr/bin/env python
__author__ = "T0x1cEnv31ope"
import os
import random
from src.main.xsys.config.CryptConfig import CryptConfig
#from Crypto.Hash import SHA256
from Crypto.Cipher import AES


class CryptoManager(CryptConfig, object):
    """
        [Description]
        __init__
        - Construct a Crawler Object
    """
    def __init__(self):
        super(CryptoManager, self).__init__()

    """
        [Description]
        encrypt
        - Encrypt a given file by a given key
        :param -> key:str - a key for encryption
        :param -> filename:file - a given file to be encrypt
    """
    def encrypt(self, key, filename):
        out_file = os.path.join(os.path.dirname(filename), self.get_suffix + os.path.basename(filename))
        file_size = str.format(os.path.getsize(filename)).zfill(self.get_byte_size)
        iv = ''
        for i in range(self.get_byte_size):
            iv += chr.__format__(random.randint(0, 0xFF))
        encrypter = AES.new(key, AES.MODE_CBC, iv)
        with open(filename, 'rb') as infile:
            with open(out_file, 'wb') as outfile:
                outfile.write(filename)
                outfile.write(iv)
                while True:
                    chunk = infile.read(self.get_chunk_size)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % self.get_byte_size != 0:
                        chunk += ' '*(self.get_byte_size - (len(chunk) % self.get_byte_size))
                    elif len(chunk) != file_size:
                        outfile.write(encrypter.encrypt(chunk))
                    else:
                        break
                outfile.close()

    """
        [Description]
        decrypt
        - Decrypt a file content given a key 
        :param -> key:str - a key for decryption
        :param -> filename:file - a given encrypted file
    """
    def decrypt(self, key, filename):
        out_file = os.path.join(os.path.basename(filename), os.path.basename(filename[12:]))
        with open(filename, 'rb') as infile:
            file_size = infile.read(self.get_byte_size)
            iv = infile.read(self.get_byte_size)
        decrypter = AES.new(key, AES.MODE_CBC, iv)
        with open(out_file, 'wb') as outfile:
            while True:
                chunk = infile.read(self.get_chunk_size)
                if len(chunk) == 0:
                    break
                outfile.write(decrypter.decrypt(chunk))
            outfile.truncate(int(file_size))


if __name__ == '__main__':
    c = CryptoManager()
