from selenium import webdriver
from selenium.webdriver.chrome.options import options

chromeoptions = options()
chromeoptions.add_experimental_options("prefs", {"download.default_directory": "C:\PycharmProjects\DownloadedFiles"})

driver = webdriver.Chrome(executable_path="C:\Driver\Chromedriver_win32\chromedriver.exe", chrome_options=chromeoptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

# download text file
driver.find_element_by_id("textbox").send_keys("anuj pal")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

# download pdf file
driver.find_element_by_id("pdfbox").send_keys("Anuj Pal")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

# driver.close()
