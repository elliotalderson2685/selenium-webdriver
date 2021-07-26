from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Driver\Chromedriver_win32\chromedriver.exe")
driver.get ("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath('/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button').click()
driver.find_element_by_xpath("//*[@id='origin']/span/input").click()

driver.close()