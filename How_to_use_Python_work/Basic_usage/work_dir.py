# 获取文件当前工作目录路径
import os
import sys

os.getcwd()    #获取当前工作目录

print("sys.path[0] = ", sys.path[0])
print("sys.argv[0] = ", sys.argv[0])
print("os.getcwd() = ", os.getcwd())

os.chdir("./GUI")   #修改当前工作目录


import os
print(os.getcwd())
print(os.path.abspath('.'))
print(os.path.abspath(os.curdir))#获取当前工作目录路径

print(os.path.abspath('..')) #获取当前工作的父目录 ！注意是父目录路径
print(os.path.abspath('.')) #获取当前工作目录路径
print(os.path.abspath('test.txt'))#获取当前目录文件下的工作目录路径


root = os.getcwd() #获得当前路径 /home/dir1
print(root)
#输出
#/home/dir1

name = "Optimization"
#定义文件名字
print(os.path.join(root, name))   #合并路径名字和文件名字，并打印
#输出
#/home/dir1/file1


srcPath = r"work_dir.py"

path = os.path.abspath(srcPath)

print("全路径为：",path)

print("路径名，文件名",os.path.split(path))
