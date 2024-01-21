'''
@Project ：webBehavioralSimulation 
@File    ：BehavioralSimulation.py
@IDE     ：PyCharm 
@Author  ：kant
@Date    ：2024/1/11 11:15 
@content :
'''
import time
import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# 调用键盘按键操作时需要引入的Keys包
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
if __name__ == '__main__':

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)#设置程序结束后不会关闭浏览器
    browser = webdriver.Chrome(options=chrome_options)

    browser.get('http://www.baidu.com/')
    browser.find_element(By.ID,"kw").send_keys("文心一言")
    browser.find_element(By.ID,"su").click()
    time.sleep(2)
    content = browser.find_elements(By.XPATH,"//a[@class='c-font-medium c-color-t opr-toplist1-subtitle_1uZgw']")
    print(type(content))
    for i in content:
        print(i.text)

    #browser.maximize_window()
    # 打印网页源代码
    #print(browser.page_source)
    actions = ActionChains(browser)
    actions.move_by_offset()







    time.sleep(5)
    #browser.quit()