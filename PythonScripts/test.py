'''
@Project ：webBehavioralSimulation 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：kant
@Date    ：2024/1/24 11:34 
@content :
'''
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
if __name__ == '__main__':
    #chrome.exe --remote-debugging-port=9223 --user-data-dir="D:\selenium\ChromeProfile9223"
    #--remote-debugging-port=9222 --user-data-dir="D:\selenium\ChromeProfile"
    # --remote-debugging-port=9223 --user-data-dir="D:\selenium\ChromeProfile9223"
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9223")
    browser = webdriver.Chrome(options=chrome_options)

    url = 'https://www.damai.cn'
    browser.get(url)
    time.sleep(1)
    browser.maximize_window()
    """
    # 获取登入按钮：/html/body/div[2]/div/div[3]/div[1]/div[1]
    browser.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[1]/div[1]').click()
    username = '15874453226'
    password = '@DaMai741852'

    time.sleep(1)
    
    # 进入iframe
    iframe = browser.find_element(By.XPATH, '//iframe[@id="alibaba-login-box"]')
    browser.switch_to.frame(iframe)
    iframe_login = browser.find_elements(By.XPATH, '//div[@class="fm-field"]/div[2]/input')
    iframe_login[0].send_keys(username)
    iframe_login[1].send_keys(password)

    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(1)
    # 退出iframe
    # browser.switch_to.default_content()
    
    # 进入第二层iframe
    
    iframe2 = browser.find_element(By.XPATH, '//iframe[@id="baxia-dialog-content"]')
    browser.switch_to.frame(iframe2)
    span = browser.find_element(By.XPATH, '//span[@id="nc_1_n1z"]')
    actions = ActionChains(browser)
    actions.move_to_element(span).perform()
    actions.click_and_hold().perform()
    time.sleep(1)
    actions.move_by_offset(300, 0).perform()
    actions.release().perform()
    """
