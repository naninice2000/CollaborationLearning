import pytest 
from selenium import webdriver
import sys
sys.path.append("../t_lib/")
from TwitterPageObject import HomePageObjectModel


chromedriver_path = "C:/Users/shrut/Documents/GitHub/CollaborationLearning/vinod/PythonTraining/chromedriver_win32/chromedriver.exe" 
driver = webdriver.Chrome(chromedriver_path)
				


def test_CheckLanding_PageTitle():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	assert "Twitter. It's what's happening" in driver.title				

def test_login_button_validation():
	driver.get("http://twitter.com")
	homepage = HomePageObjectModel()
	we=driver.find_element_by_xpath(homepage.get_login_button_we())
	we.click()
	driver.implicitly_wait(10)
	message = driver.find_element_by_id(homepage.get_login_message_after_click()) 
	print message.text
	assert message.text in "Log in to Twitter"
	

def test_signup_button_validation():
	driver.get("http://twitter.com")
	homepage = HomePageObjectModel()
	signup_button = driver.find_element_by_xpath(homepage.get_signup_button_we())
	signup_button.click()
	driver.implicitly_wait(10)
	nextpage = driver.find_element_by_xpath(homepage.get_signup_button_click())
	print nextpage.text
	assert nextpage.text in "Join Twitter today."
	driver.quit()


