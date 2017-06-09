from selenium import webdriver
import pytest 


chromedriver_path = "/Users/Nikhil Mesineni/Documents/workspace/new training/chromedriver_win32/chromedriver.exe"

def testCheckLandingPageTitle():
	 driver = webdriver.Chrome(chromedriver_path)
 	 driver.get("http://twitter.com")
 	 assert "Twitter. It's what's happening" in driver.title
 	 driver.quit()


def testSingupButton():
	 driver = webdriver.Chrome(chromedriver_path)
	 driver.get("http://twitter.com")
	 we = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[2]")
	 we.click()
	 driver.implicitly_wait(10)
	 full_name_we = driver.find_element_by_id("full-name")
	 full_name_we.send_keys("Nikhil Mesineni")
	 driver.implicitly_wait(10)
	 email_id = driver.find_element_by_id("email")
	 email_id.send_keys("nikhilraomesineni@gmail.com")
	 password_id = driver.find_element_by_id("password")
	 password_id.send_keys("nikhilmesineni")
	 we_signup = driver.find_element_by_xpath("//*[@id=\"phx-signup-form\"]/div[3]/div")
	 we_signup.click()
	
