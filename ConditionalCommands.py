from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Driver\Chromedriver_win32\chromedriver.exe")

driver.get ("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath('/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button').click()

driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[1]/a[1]").click()
user_ele = driver.find_element_by_name("userId")
print(user_ele.is_displayed())
print(user_ele.is_enabled())
user_ele.send_keys("apaul2685")

pwd_ele = driver.find_element_by_name("pwd")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())
pwd_ele.send_keys("@Anujpal2685@")

time.sleep(10)

driver.find_element_by_xpath("//*[@id='login_header_disable']/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button").click()

from_city=driver.find_element_by_xpath("//*[@id='origin']/span/input")
print(from_city.is_displayed())
print(from_city.is_enabled())
from_city.send_keys("KANPUR CENTRAL - CNB")

to_city = driver.find_element_by_xpath("//*[@id='destination']/span/input")
print(to_city.is_displayed())
print(to_city.is_enabled())
to_city.send_keys("ORAI - ORAI")

j_date = driver.find_element_by_xpath("//*[@id='jDate']/span/input")
print(j_date.is_displayed())
print(j_date.is_enabled())
j_date.send_keys("10/06/2021")

driver.find_element_by_xpath("//*[@id='divMain']//div/button")
