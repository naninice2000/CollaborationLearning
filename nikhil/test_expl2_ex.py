from selenium import webdriver
import pytest 


chromedriver_path = "/Users/Nikhil Mesineni/Documents/workspace/new training/chromedriver_win32/chromedriver.exe"

'''def testCheckLandingPageTitle():
	 driver = webdriver.Chrome(chromedriver_path)
 	 driver.get("http://twitter.com")
 	 assert "Twitter. It's what's happening" in driver.title'''



def testLoginbutton():
	 driver = webdriver.Chrome(chromedriver_path)
	 driver.get("http://twitter.com")
 	 we_login =driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[3]")
 	 we_login.click()
	 driver.implicitly_wait(10)
	 email_id = driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/div[1]/input")
	 email_id.send_keys("nikhilraomesineni@gmail.com")
	 password = driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/div[2]/input")
	 password.send_keys("nikilmesneni")
	 we_login =driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/input[1]")
	 we_login.click()
	 driver.implicitly_wait(10)
	 error_message = driver.find_element_by_xpath("//*[@id=\"message-drawer\"]/div/div/span")
	 print error_message.text
	 assert error_message.text == "The email and password you entered did not match our records. Please double-check and try again."
	 
	