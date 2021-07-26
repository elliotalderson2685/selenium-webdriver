from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Driver\Chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button').click()

time.sleep(5)

#driver.switch_to.alert.accept() #dismiss pop up with OK button

driver.switch_to.alert.dismiss() # dismiss pop up with cancel button

driver.close()
