import pytest 
from selenium import webdriver
import sys
sys.path.append("../t_ie_lib/")
from DataParser import *
from TwitterPageObject import HomePageObjectModel
from ConfigReader import ConfigReader
#from testconfig import *



Ie_path="C:/Users\shrut/Documents/GitHub/CollaborationLearning/vinod/PythonTraining/iedriver/IEDriverServer.exe"
driver = webdriver.Ie(Ie_path)
data_parser = dataParser("../t_ie_input/homepage_testdata.csv")
data_parser.constructDataSet()


	
#CR =("../t_config/config.json")			


'''def test_CheckLanding_PageTitle():
	#dr = getPortocolInfo+"://"+ getPortalIP

	#driver.get(dr)
	driver.get("http://twitter.com")

	data_map = data_parser.getTestCaseData("1")
	#data_map = str(data_map)
	assert  driver.tittle in data_map["expectedResult"] '''

def test_login_button_validation():
	
	driver.get("http://twitter.com")
	
	homepage = HomePageObjectModel()
	we=driver.find_element_by_xpath(homepage.get_login_button_we())
	we.click()
	driver.implicitly_wait(10)
	message = driver.find_element_by_id(homepage.get_login_message_after_click()) 
	data_map = data_parser.getTestCaseData("2")
	assert message.text in data_map["expectedResult"]
	

'''def test_signup_button_validation():
	driver.get("http://twitter.com")
	homepage = HomePageObjectModel()
	signup_button = driver.find_element_by_xpath(homepage.get_signup_button_we())
	signup_button.click()
	driver.implicitly_wait(10)
	nextpage = driver.find_element_by_xpath(homepage.get_signup_button_click())
	print nextpage.text
	assert nextpage.text in "Join Twitter today."'''

  
'''def test_invalidecredential_loginbutton():
	driver.get("http://twitter.com")
	homepage = HomePageObjectModel()
	we=driver.find_element_by_xpath(homepage.get_login_button_we())
	we.click()
	driver.implicitly_wait(10)
	username = driver.find_element_by_name(homepage.get_username_input_we())
	username.send_keys("abcd")
	password = driver.find_element_by_name(homepage.get_passw_button_we())
	password.send_keys("abcd")
	login_button = driver.find_element_by_xpath(homepage.get_login_loginpage())
	login_button.click()
	driver.implicitly_wait(10)
	login= driver.find_element_by_xpath(homepage.get_invalide_credentials_message())
	assert login.text in "The username and password you entered did not match our records. Please double-check and try again."

'''