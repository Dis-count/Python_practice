# pip install splinter

# coding=utf-8

import time
from splinter import Browser

def splinter(url):
    browser = Browser()
    #login 126 email websize
    browser.visit(url)
    #wait web element loading
    time.sleep(5)
    #fill in account and password
    browser.find_by_id('idInput').fill('xxxxxx')
    browser.find_by_id('pwdInput').fill('xxxxx')
    #click the button of login
    browser.find_by_id('loginBtn').click()
    time.sleep(8)
    #close the window of brower
    browser.quit()

if __name__ == '__main__':
    websize = 'https://mail.163.com/'
    splinter(websize)
