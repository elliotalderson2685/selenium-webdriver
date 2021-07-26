from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Driver\Chromedriver_win32\chromedriver.exe")
driver.get ("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
print(driver.title)
driver.execute_script("window.scrollTo(0,document.body.10)")
driver.find_element_by_xpath("//*[@id='origin']/span/input").click ()
driver.close()