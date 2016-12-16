# coding=utf-8

import os
import re

rootDir = '/Users/username/Desktop/cc'
path = '/Users/username/Desktop/allFunction.txt'
count = 0

def find_all_unused_func_list():
    f = open(path, 'r')
    for line in f.readlines():
        func_name = line.strip()
        find_all_func_list(func_name)

def find_all_func_list(funcname):
    global count
    count = 0
    for root,dirs,files in os.walk(rootDir):
        for filespath in files:
            filename = os.path.join(root,filespath)
            if filename.endswith(".swift") or filename.endswith(".m") or filename.endswith(".h"):
                readContent(filename,funcname)
    if count == 1:
        print "未调用方法：",funcname

def readContent(filename,funcname):
    global count
    f = open(filename, 'r')
    for line in f.readlines():
        m = re.search(r'(%s)'%(funcname), line)
        if m:
            count += 1
    return 

if __name__ == '__main__':
    find_all_unused_func_list()











