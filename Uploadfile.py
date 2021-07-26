from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = 'C:\Driver\Chromedriver_win32\chromedriver.exe')
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.switch_to.frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C://PycharmProjects/FilesToUpload/DefaultWallpaper.jpg")




