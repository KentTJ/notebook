#coding=utf-8
import os
import shutil
from os import path
from subprocess import Popen, PIPE, STDOUT
import os
import datetime  as dt
import subprocess

#print  "======source build/envsetup.sh========"
#os.system("source build/envsetup.sh")

#print  "======lunch aosp_sailfish-userdebug======="
#os.system("lunch aosp_sailfish-userdebug")



def execShellCommand(cmd):
    print  "================cmd================="
    print cmd
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,executable="/bin/bash")
    while True:  
        buff = p.stdout.readline()
        buff = buff.strip()   #strip
        #if (buff == '' or  buff == "" or buff == ' '  or len(buff) == 0 or buff==None  or buff=='\n' or buff.strip()=='') and p.poll() != None:  #bu da log
        if (buff == '' or  buff == "" or buff == ' '  or len(buff) == 0 or buff==None  or buff=='\n' or buff.strip()==''):  #bu da log
            break
        #print(repr(buff))


        now_time = dt.datetime.now().strftime('%F %T')
        print now_time + " " + buff
    p.wait()


def copyFile(orgin_path, target_path):
    print "========================="
    print "orgin_path: " + orgin_path
    print "target_path: " + target_path
    try:
        shutil.copy(orgin_path, target_path)
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())


def main():

    os.chdir("./replaceFiles/")
    os.system("python replaceFiles.py")

    #参数
    rootPath = "/home/chengang/workingSpace/aosp_android1000_r17"
    os.chdir(rootPath)
    
    
    execShellCommand("pwd")
    execShellCommand("source build/envsetup.sh")
    # not work
    execShellCommand("lunch aosp_sailfish-userdebug")
    execShellCommand("make framework -j16")
    execShellCommand("make services -j16")
    
    #execShellCommand("cp  /home/chengang/workingSpace/aosp_android_800r13/out/target/product/sailfish/system/framework/framework.jar  /home/chengang/workingSpace/local/python_install/jars ")
    #execShellCommand("cp  /home/chengang/workingSpace/aosp_android_800r13/out/target/product/sailfish/system/framework/services.jar  /home/chengang/workingSpace/local/python_install/jars ")

    copyFile(rootPath + '/out/target/product/sailfish/system/framework/framework.jar', '/home/chengang/workingSpace/local/aosp_android1000_r17/python_install/jars')
    copyFile(rootPath + '/out/target/product/sailfish/system/framework/services.jar', '/home/chengang/workingSpace/local/aosp_android1000_r17/python_install/jars')
    
    print  "================end================="


if __name__ == "__main__":
    main()