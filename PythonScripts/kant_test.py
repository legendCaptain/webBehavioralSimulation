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
    url = 'https://buy.tmall.com/order/confirm_order.htm?x-itemid=20739895092&spm=pc_detail.27183998/evo365560b447259&x-uid=3408119730'
    browser.get(url)
    browser.maximize_window()
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[1]/div[1]/div/div[9]/div/div/a').click()