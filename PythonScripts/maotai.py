'''
@Project ：webBehavioralSimulation 
@File    ：maotai.py
@IDE     ：PyCharm 
@Author  ：kant
@Date    ：2024/2/23 15:31 
@content :
'''
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9223")
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)
    url = 'https://chaoshi.detail.tmall.com/item.htm?addressId=14208833635&from_scene=B2C&id=20739895092&skuId=4227830352490&spm=a3204.17725404.9886497900.1'
    browser.get(url)
    browser.maximize_window()
    #browser.find_element(By.XPATH, '//*[text()="马上抢"]|//*[text()="立即购买"]').click()
    #browser.find_element(By.XPATH,'//*[text()="提交订单"]').click()
    #browser.find_element(By.XPATH,'//input[@type="password"]').send_keys('868788')
    #browser.find_element(By.XPATH,'//input[@value="确定"]')

    #时间控制
    while(True):
        if (str(datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')) == '20240225200000'):
            browser.refresh()
            print(f"{str(datetime.strftime(datetime.now(), '%Y%m%d%H%M%S'))}")
            browser.find_element(By.XPATH, '//*[text()="马上抢"]|//*[text()="立即购买"]').click()
            #browser.find_element(By.XPATH,'//*[text()="提交订单"]').click()
            #提交订单
            browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[1]/div/div[9]/div/div/a').click()
            break