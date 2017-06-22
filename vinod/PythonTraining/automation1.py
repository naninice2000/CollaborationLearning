from selenium import webdriver
import pytest 

chromedriver_path = "C:/Users/shrut/Documents/GitHub/CollaborationLearning/vinod/PythonTraining/chromedriver_win32/chromedriver.exe"

'''def testCheckLandingPageTitle():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	assert "Twitter. It's what's happening" in driver.title
	driver.quit()'''


'''def testSingupButton():
 driver = webdriver.Chrome(chromedriver_path)
 driver.get("http://twitter.com")
 we = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[2]")
 print we.text
 driver.quit()'''

'''def testSingupButton():

 	driver = webdriver.Chrome(chromedriver_path)
 	driver.get("http://twitter.com")
 	we = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[2]")
 	we.click()
 	driver.implicitly_wait(10)
 	full_name_we = driver.find_element_by_id("full-name")
 	full_name_we.send_keys("Venkat Ram")
 	#driver.implicitly_wait(10)
	email_id = driver.find_element_by_id("email")
	email_id.send_keys("ram@gmail.com")
	password = driver.find_element_by_id("password")
	password.send_keys("reddy")
	we_sign =driver.find_element_by_xpath("//*[@id=\"phx-signup-form\"]/div[3]/div")
	we_sign.click()
'''

 

def testLoginbutton():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	we_login =driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[3]")
	we_login.click()
	driver.implicitly_wait(10)
	email_id = driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/div[1]/input")
	#email_id = driver.find_element_by_name("username_or_email")
	email_id.send_keys("vinodkumar.adama@gmail.com")
	password = driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/div[2]/input")
	password.send_keys("reddy")
	we_login1 =driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/input[1]")
	we_login1.click()
	driver.implicitly_wait(10)


'''def testBlanksigninbutton():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	we_sign3 =driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[3]")
	we_sign3.click()
	driver.implicitly_wait(10)
	we_sign1 =driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/input[1]")
	we_sign1.click()
	'''





'''def testfeaturebutton():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	feature = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[2]/div/a[1]/span")
	feature.click()'''







