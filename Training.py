import unittest
from selenium import webdriver
class NewTest1(unittest.TestCase):
#classmethod
def setUpClass(self):
    print('inside setup class')
#classmethod
def tearDownClass(self):
    print('inside teardown class')
def setUp(self):
    print('inside setup')
def tearDown(self):
    print('inside tear down')
def test_launch_google_home_page(self):
    driver=webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    driver.get('http://www.google.co.in')
    driver.maximize_window()
    self.assertEqual(driver.title,'Google','This title doesnot match')
def test_launch_abc_page(self):
    print("inside test 2")

unittest.main(argv=[''],verbosity=3,exit=False)
