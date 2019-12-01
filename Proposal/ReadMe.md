# 将Py转为exe可执行文件
    pyinstaller -F -w -i manage.ico app.py

* -F：打包为单文件
* -w：Windows程序，不显示命令行窗口
* -i：是程序图标，app.py是你要打包的py文件


    
    如果是下载github上的包之后手动安装，那么步骤是
    
    打开cmd，切到pyinstaller解压包目录，直接放在c盘目录下了，所以操作是
    cd C:\pyinstaller-develop
    
    安装pyinstaller 操作是:
    进目录后输入python setup.py install


> 安装方法：       先跑`pip install pywin32`再跑  `pip install pyinstaller` 即可


