import os
import time
from shutil import copyfile

# 这里假设client电脑上要输出的文件夹在BASE_DIR 下，网盘路径在NET_DIR目录下
BASE_DIR = 'server/'
NET_DIR  = 'net/'


def main():
    while True:
        filenames = os.listdir(NET_DIR)
        for filename in filenames:
            print("downloading {} into local disk...".format(filename))
            copyfile(NET_DIR+filename,BASE_DIR+filename)
            os.remove(NET_DIR+filename)
            print('downloaded {} into local disk.'.format(filename))
        time.sleep(3)


if __name__ == '__main__':
    main()
