# coding=utf-8

import os
import re

rootDir = 'aa/bb/cc'
s = set()

def find_all_func_list(rootDir):
    for root,dirs,files in os.walk(rootDir):
        for filespath in files:
            filename = os.path.join(root,filespath)
            if filename.endswith(".swift"):
                readContent(filename)

def readContent(path):
    f = open(path, 'r')
    for line in f.readlines():
        m = re.search(r'func\s+(\w+)\s*\(', line)
        if m:
            print m.group(0)
            s.add(m.group(1))

    save_path = 'allFunction.txt'
    func_list = '\n'.join(sorted(s))
    os.system('echo "%s" > %s' % (func_list, save_path))

if __name__ == '__main__':
    find_all_func_list(rootDir)











