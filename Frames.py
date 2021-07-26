from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='C:\Driver\Chromedriver_win32\chromedriver.exe')
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
driver.maximize_window()
driver.switch_to.frame("globalSqa")
driver.find_element_by_link_text("Platform & Database Testing").click()

driver.switch_to.default_content()
driver.switch_to.frame("google_esf")
driver.find_element_by_link_text("Home").click()

print(driver.current_url)
