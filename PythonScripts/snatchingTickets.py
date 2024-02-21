'''
@Project ：webBehavioralSimulation 
@File    ：snatchingTickets.py
@IDE     ：PyCharm 
@Author  ：kant
@Date    ：2024/2/19 10:43 
@content :
'''
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
if __name__ == '__main__':
    start_time = time.time()
    #1.开启远程调试浏览器
    # chrome.exe --remote-debugging-port=9222 --user-data-dir="E:\selenium\ChromeProfile"
    #chrome.exe --remote-debugging-port=9223 --user-data-dir="D:\selenium\ChromeProfile9223
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9223")
    browser = webdriver.Chrome(options=chrome_options)

    #2.在浏览器中搜索内容地址
    url = 'https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_4.591b23e19OX1Ef&ctl=%E5%B1%95%E8%A7%88%E4%BC%91%E9%97%B2&order=1&cty=%E5%8C%97%E4%BA%AC'
    print('1:获取网址')
    browser.get(url)
    browser.maximize_window()
    print('1:获取网址，完成')
    time.sleep(5)

    #3.找到网址中所需内容
    print('2:找到网址中所需内容')
    browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[3]/div/div[1]/a').click()
    print('2:找到网址中所需内容，完成')
    time.sleep(5)
    #4.如果产生了多个标签页，获取所有窗口句柄，找到所需的标签窗口
    window_handles = browser.window_handles
    # 切换到新标签页
    print('3:切换到新标签页')
    browser.switch_to.window(window_handles[1])
    print('3:切换到新标签页，完成')
    # 切换回原始标签页
    #driver.switch_to.window(window_handles[0])
    time.sleep(5)
    #5.找到购买按钮(不，立即购买)，并点击
    print('4:找到购买按钮(不，立即购买)，并点击')
    browser.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div[3]/div[9]/div/div[3]/div[3]').click()
    print('4:找到购买按钮(不，立即购买)，并点击，完成')
    time.sleep(5)
    #6.点击提交订单按钮
    print('5:点击提交订单按钮')
    browser.find_element(By.XPATH,'/html/body/div[2]/div/div[5]/div[2]/div/div[2]/div[2]/div[2]/span').click()
    print('5:点击提交订单按钮，完成')
    #点击继续浏览器支付宝
    time.sleep(5)
    print('6:点击继续浏览器支付宝')
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[1]/button[2]').click()
    print('6:点击继续浏览器支付宝，完成')
    time.sleep(5)

    print('11:确认付款')
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/button').click()
    print('11:确认付款，完成')
    print('12:输入密码')

    time.sleep(5)
    password = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/div')
    ActionChains(browser).move_to_element(password).click().send_keys('******').perform()
    print('12:输入密码，完成')
    finish_time = time.time()
    print(f'整体时间：{finish_time-start_time}')