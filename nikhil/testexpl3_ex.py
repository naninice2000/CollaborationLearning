from selenium import webdriver
import pytest 

chromedriver_path = "/Users/Nikhil Mesineni/Documents/workspace/new training/chromedriver_win32/chromedriver.exe"

def testusername_error():
	 driver = webdriver.Chrome(chromedriver_path)
	 driver.get("http://twitter.com")
	 click_signup = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[2]")
	 click_signup.click()
	 driver.implicitly_wait(10)
	 full_name_we = driver.find_element_by_id("full-name")
	 full_name_we.send_keys("  ")
	 driver.implicitly_wait(10)
	 error_message = driver.find_element_by_xpath("//*[@id=\"phx-signup-form\"]/div[1]/div[1]/div/div/p[2]")
	 print error_message.text
	 assert error_message.text in "What's your name?"
	 #driver.quit()
	