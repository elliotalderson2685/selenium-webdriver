from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Driver\Chromedriver_win32\chromedriver.exe")

driver.get("https://www.facebook.com/")
time.sleep(5)
print(driver.title)

driver.get("https://www.instagram.com/")
time.sleep(5)
print(driver.title)

driver.back()
time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)

