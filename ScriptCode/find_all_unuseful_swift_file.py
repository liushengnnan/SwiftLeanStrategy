# coding=utf-8
import glob
import os
import re

rootDir = '/Users/username/Desktop/cc'
path = '/Users/username/Desktop/cc/dd'

def scan_files(directory,prefix=None,postfix=None):
  files_list=[]
   
  for root, sub_dirs, files in os.walk(directory):
    for special_file in files:
      if postfix:
        if special_file.endswith(postfix):
          filename = os.path.join(root,special_file)
          files_list.append(filename)
      elif prefix:
        if special_file.startswith(prefix):
          filename = os.path.join(root,special_file)
          files_list.append(filename)
      else:
        files_list.append(os.path.join(root,special_file))
  return files_list

def find_un_used_swiftfile():
    swift_list = scan_files(rootDir, postfix=".swift")
    swift_filename = [os.path.basename(pic)[:-6] for pic in swift_list]
    unused_swift = []
    
    for i in range(0, len(swift_list)):
        pic_name = swift_filename[i]
        command = 'ag --ignore-dir Pods -l "%s" %s' % (pic_name, path)
        result = os.popen(command).read()
        ary = result.split('\n')

        if len(ary) == 3 :
          unused_swift.append(swift_list[i])
          print 'unUsedswift："%s" \n%s' % (pic_name ,result)

    swift_path = 'unUsedSwift.txt'
    swifttex = '\n'.join(sorted(unused_swift))
    os.system('echo "%s" > %s' % (swifttex, swift_path))

    print 'unuse res:%d' % (len(unused_swift))
    print 'Done!'

if __name__ == '__main__':
    find_un_used_swiftfile()
