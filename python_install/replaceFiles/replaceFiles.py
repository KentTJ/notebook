#coding=utf-8
import os
import shutil
from os import path
from subprocess import Popen, PIPE, STDOUT
import os
import subprocess

def execShellCommand(cmd):
    print  "================cmd================="
    print cmd
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,executable="/bin/bash")
    while True:  
        buff = p.stdout.readline()  
        if buff == '' and p.poll() != None:  
            break
        print buff
    p.wait()


def copyFile(windowS_path, linuxS_path):
    print "========================="
    print "windowS_path: " + windowS_path
    print "linuxS_path: " + linuxS_path
    try:
        shutil.copy(windowS_path, linuxS_path)
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())
    
    
def CopyWindowS_path2linuxS_path(filename, preLinux, prewindow):
    pos = []
    linuxS = []
    windowS = []
    with open(filename, 'r') as file_to_read:
        while True:
            lines = file_to_read.readlines() # 整行读取数据
            if not lines:
                break
                pass
            for i in lines:
                i = '/'.join(i.split('\\'))  # transform the windows path to linux path
                if (len(i)==0) or (len(i[0]) == 0) or i[0].strip()=='':
                    continue

                i = i.strip().split('frameworks')
                print "========1111======="
                print i
                print "i[0]: " + i[0]
                print "i[1]: " + i[1]

                linuxS.append(preLinux + '/frameworks' + i[1])
                windowS.append(prewindow + '/frameworks' + i[1])

        print windowS
        print linuxS

        #execShellCommand("cp  $windowS_path  $linuxS_path")
        for i in range(len(windowS)):
            copyFile(windowS[i], linuxS[i])

    
    



 
def main():
    #参数：
    filename = 'barrierFree.txt' # txt文件和当前脚本在同一目录下，所以不用写具体路径
    preLinux = '/home/chengang/workingSpace/aosp_android1000_r17'
    prewindow = '/home/chengang/workingSpace/local/aosp_android1000_r17/aosp_android1000_r17'

    #复制文件
    print "=======Copy Files Begins======="
    CopyWindowS_path2linuxS_path(filename, preLinux, prewindow)



    #其他
    rootPath = "/home/chengang/workingSpace/aosp_android1000_r17/"
    os.chdir(rootPath)
    #execShellCommand("pwd")
    #execShellCommand("source build/envsetup.sh")
    # not work
    #execShellCommand("lunch aosp_sailfish-userdebug")
    #execShellCommand("make framework -j8")
    #execShellCommand("make services -j8")
    #execShellCommand("cp  /home/chengang/workingSpace/aosp/out/target/product/sailfish/system/framework/framework.jar  /home/chengang/workingSpace/local/python_install/jars ")
    #execShellCommand("cp  /home/chengang/workingSpace/aosp/out/target/product/sailfish/system/framework/services.jar  /home/chengang/workingSpace/local/python_install/jars ")

if __name__ == "__main__":
    main()