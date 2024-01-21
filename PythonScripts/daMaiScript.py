import time

from selenium.webdriver.common.by import By

# 调用键盘按键操作时需要引入的Keys包
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

if __name__ == '__main__':

    url = 'https://www.damai.cn'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)  # 设置程序结束后不会关闭浏览器
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()

    browser.get(url)
    time.sleep(1)
    #获取登入按钮：/html/body/div[2]/div/div[3]/div[1]/div[1]
    browser.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div[1]/div[1]').click()
    username = '15874453226'
    password = '@DaMai741852'

    time.sleep(1)
    #进入iframe
    iframe = browser.find_element(By.XPATH,'//iframe[@id="alibaba-login-box"]')
    browser.switch_to.frame(iframe)
    iframe_login = browser.find_elements(By.XPATH,'//div[@class="fm-field"]/div[2]/input')
    iframe_login[0].send_keys(username)
    iframe_login[1].send_keys(password)
    browser.find_element(By.XPATH,'//button[@type="submit"]').click()
    time.sleep(1)
    #退出iframe
    #browser.switch_to.default_content()

    #进入第二层iframe

    iframe2 = browser.find_element(By.XPATH, '//iframe[@id="baxia-dialog-content"]')
    browser.switch_to.frame(iframe2)
    span = browser.find_element(By.XPATH,'//span[@id="nc_1_n1z"]')
    actions = ActionChains(browser)
    actions.move_to_element(span).perform()
    actions.click_and_hold().perform()
    time.sleep(1)
    actions.move_by_offset(300,0).perform()
    actions.release().perform()


    #找不到输入框

    #print(2222)

