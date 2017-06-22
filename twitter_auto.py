from selenium import webdriver
import pytest 
from homepage_ex import HomePageObjectModel

chromedriver_path = "/Users/Nikhil Mesineni/Documents/workspace/new training/chromedriver_win32/chromedriver.exe"

def test_login_button_validation():
	 driver = webdriver.Chrome(chromedriver_path)
 	 driver.get("http://twitter.com")
	 homepage=HomePageObjectModel()
	 we = driver.find_element_by_xpath(homepage.get_login_button_we())
	 we.click()
	 driver.close()
def test_signup_button_validation():
	 driver = webdriver.Chrome(chromedriver_path)
 	 driver.get("http://twitter.com")
	 homepage=HomePageObjectModel()
	 we = driver.find_element_by_xpath(homepage.get_signup_button_we())
	 we.click()
	 driver.close()
 def test_sports_button_validation():
	 driver = webdriver.Chrome(chromedriver_path)
 	 driver.get("http://twitter.com")
	 homepage=HomePageObjectModel()
	 we = driver.find_element_by_xpath(homepage.get_sports_button_we())
	 we.click()
	 driver.close()
 
 