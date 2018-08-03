from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

drv = webdriver.Remote("http://127.0.0.1:9515", DesiredCapabilities.CHROME)

drv.get("http://www.amazon.co.jp")
drv.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys("インストラクショナルデザイン")
drv.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input').click()
