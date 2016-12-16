# coding=utf-8
import glob
import os
import re

path = 'aa/bb/cc'

images = glob.glob('aa/bb/cc/Res/images.xcassets/*/*.imageset')

def find_un_used():
    img_names = [os.path.basename(pic)[:-9] for pic in images]
    unused_imgs = []

    for i in range(0, len(images)):
        pic_name = img_names[i]
        command = 'ag "%s" %s' % (pic_name, path)
        result = os.popen(command).read()
        if result == '':
            unused_imgs.append(images[i])
            print 'unuseful_imageset: %s' % (images[i])
#            os.system('rm -rf %s' % (images[i]))

    text_path = 'unusedImagesAssets.txt'
    tex = '\n'.join(sorted(unused_imgs))
    os.system('echo "%s" > %s' % (tex, text_path))
    print 'unuse res:%d' % (len(unused_imgs))
    print 'Done!'

if __name__ == '__main__':
    find_un_used()
