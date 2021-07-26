from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = "C:\Driver\Chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("http://demo.guru99.com/test/newtours/index.php")

links = driver.find_elements(By.TAG_NAME,"a")

print(len(links))

for link in links :
    print(link.text)

driver.find_element(By.LINK_TEXT,"REGISTER").click()

