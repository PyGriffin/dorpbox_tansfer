
import os 
import shutil import copyfile
import time

# 这里假设需要传输的数据都在BASE_DIR 目录下，网盘路径为NET_DIR   
BASE_DIR = 'server/'
NET_DIR  = 'net/'


def main():
    # 获取所有文件
    filenames = os.listdir(BASE_DIR)
    for i,filename in enumerate(filenames):
        print("copying {} into net dirve... {}/{}".format(filename,i+1, len(filenames)))
        # 将文件从基础目录拷贝到云盘目录
        copyfile(BASE_DIR+filename,NET_DIR+filename)
        print("copied {} into net dirve,waiting client complete... {}/{}".format(fileename,i+1,len(filenames)))
        
        while os.path.exists(NET_DIR+filename):
            time.sleep(3)
    
    print("transferred {} into client. {}/{}".format(fileename,i+1,len(filenames)))


if __name__ == '__main__':
    main()


