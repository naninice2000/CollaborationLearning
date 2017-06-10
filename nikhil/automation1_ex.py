from selenium import webdriver
import pytest 

chromedriver_path = "/Users/Nikhil Mesineni/Documents/workspace/new training/chromedriver_win32/chromedriver.exe"

def testCheckLandingPageTitle():
	driver = webdriver.Chrome("/Users/Nikhil Mesineni/Documents/workspace/new training/chromedriver_win32/chromedriver.exe")
 	driver.get("http://twitter.com")
 	assert "Twitter. It's what's happening" in driver.title
 	driver.quit()

'''
def testSingupButton():
 driver = webdriver.Chrome("/Users/Nikhil Mesineni/Documents/workspace/new training/chromedriver_win32/chromedriver.exe")
 driver.get("http://twitter.com")
 we = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[2]")
 print we.text
 driver.quit()
 '''