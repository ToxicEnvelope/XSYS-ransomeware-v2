#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "T0x1cEnv31ope"
import os
import time
import argparse
from src.main.xsys.config.CrawlerConfig import CrawlerConfig


class Crawler(CrawlerConfig, object):
    """
        [Description]
        __init__
        - Construct a Crawler Object
    """
    def __init__(self):
        super(Crawler, self).__init__()

    """
        [Description]
        _recurse
        - this method will recurse over a given path and
          and build a GUI display pattern of all files under it. 
    """
    def _recurse(self, parent_path, file_list, prefix, output_buf, level):
        try:
            if len(file_list) == 0 \
                    or (self.max_level != -1 and self.max_level <= level):
                return
            else:
                file_list.sort(key=lambda f: os.path.isfile(os.path.join(parent_path, f)))
                for idx, sub_path in enumerate(file_list):
                    if any(exclude_name in sub_path for exclude_name in self.exn):
                        continue

                    full_path = os.path.join(parent_path, sub_path)
                    idc = "┣━"
                    if idx == len(file_list) - 1:
                        idc = "┗━"

                    if os.path.isdir(full_path) and sub_path not in self.exf:
                        output_buf.append('{0}{1}[{2}]'.format(prefix, idc, sub_path))
                        if len(file_list) > 1 and idx != len(file_list) - 1:
                            tmp_prefix = prefix + "┃  "
                        else:
                            tmp_prefix = prefix + "\t"
                        self._recurse(full_path, os.listdir(full_path), tmp_prefix, output_buf, level + 1)
                    elif os.path.isfile(full_path):
                        output_buf.append('{0}{1}{2}'.format(prefix, idc, sub_path))
        except Exception as err:
            print('\n[Error]\n{0}'.format(err))
            pass

    """
        [Description]
        make
        - this method responsible to handle to _recurse
          function and return the built tree as output.
        
        :param -> given arguments from the system
        :returns ->  output string pattern
    """
    def make(self, args):
        self.root = args.root
        self.exf = args.exclude_folder
        self.exn = args.exclude_name
        self.max_level = args.max_level

        print("root: {0}".format(self.root))

        buf = []
        path_parts = self.root.rsplit(os.path.sep, 1)
        buf.append('{0}'.format(path_parts[-1],))
        self._recurse(self.root, os.listdir(self.root), "", buf, 0)

        output_str = "\n".join(buf)
        if len(args.output) != 0:
            with open(args.output, 'w') as of:
                of.write(output_str)
        return output_str

    """
        [Description]
        recursive_file_crawler
        - Create a Hierarchical Tree to index all files in the system
          implementing: tree height = (nodes^2+1) -1 < leafs :- simplifying -1:LEFT, null:RIGHT equation
        
        :return -> a Tree of OS files  
    """
    def recursive_file_crawler(self, tree=[], items=[], queue=[]):
        if not items and not queue:
            return self.recursive_file_crawler(tree, [], [])
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

    """
        [Description]
        linear_file_crawler
        - Create a list of files form current working directory and return the list.
        
        :return -> list of files
    """
    @staticmethod
    def linear_file_crawler():
        print('[ SCANNING {0} ]'.format(os.getcwd()))
        all_files = []
        start_time = int(round(time.time() * 1000))
        for root, dirs, files in os.walk(os.getcwd()):
            for names in files:
                all_files.append(os.path.join(root, names))
        end_time = int(round(time.time() * 1000))
        return all_files, (end_time-start_time)/1000


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--root", help="root of file tree", default=".")
    parser.add_argument("-o", "--output", help="output file name", default="")
    parser.add_argument("-xf", "--exclude_folder", nargs='*', help="exclude folder", default=[])
    parser.add_argument("-xn", "--exclude_name", nargs='*', help="exclude name", default=[])
    parser.add_argument("-m", "--max_level", help="max level",
                        type=int, default=-1)
    args = parser.parse_args()
    print(Crawler().make(args))
