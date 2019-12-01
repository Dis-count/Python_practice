import getpass

_username = "Discount"
_passwd = "abc,123"
username = input("请输入你的用户名： ")
#getpass这个模块可以帮助你输入密码时把密码隐藏
passwd = getpass.getpass("请输入你的密码： ")

if username == _username and passwd == _passwd:
    print("你的用户名密码输入正确。")
else:
    print("你的用户名或者密码错误！")
