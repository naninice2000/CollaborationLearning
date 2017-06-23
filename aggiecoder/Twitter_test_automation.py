import os
from selenium import webdriver

chromedriver_path = "C:/Users/Sam/Documents/py_workspace/chromedriver_win32/chromedriver.exe"

def testCheckLandingPageTitle():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	assert "Twitter. It's what's happening" in driver.title
	#driver.quit()

def testSignupButton():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	we = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[2]")
	we.click()
	driver.implicitly_wait(10)
	full_name_we = driver.find_element_by_id("full-name")
	full_name_we.send_keys("happy")
	#driver.implicitly_wait(10)
	email_id = driver.find_element_by_id("email")
	email_id.send_keys("lasflanfaubbefa@gmail.com")
	password_id = driver.find_element_by_id("password")
	password_id.send_keys("Checkmate123")
	signup_id = driver.find_element_by_id("submit_button")
	signup_id.click()
	phone_number = driver.find_element_by_xpath('//*[@id="device_address"]')
	phone_number.send_keys("924-757-3889")
	click_next = driver.find_element_by_xpath('//*[@id="phone_number_btn"]')
	click_next.click()
	driver.quit()
	
def testSignupButtonError():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	sign_up = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[2]")
	sign_up.click()
	driver.implicitly_wait(10)
	full_name_we = driver.find_element_by_id("full-name")
	full_name_we.send_keys(" ")
	driver.implicitly_wait(10)
	error_message = driver.find_element_by_xpath('//*[@id="phx-signup-form"]/div[1]/div[1]/div/div/p[2]')
	print error_message.text
	assert error_message.text in "What's your name?"

def testLoginButton():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	
	#finds login button and clicks on it
	we = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[3]")
	we.click()
	driver.implicitly_wait(10)
	
	#finds and enters in username
	email_we = driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/div[1]/input")
	email_we.send_keys("samiboy18@rocketmail.com")
	
	#finds and enters in password
	password = driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/div[2]/input")
	password.send_keys("Holybible2")
	
	#logs in
	login_button = driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/input[1]")
	login_button.click()
	print("Succesfully logged in")

def testSportsButton():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	
	#finds sport button and clicks on it
	we = driver.find_element_by_xpath('//*[@id="doc"]/div[1]/div/div[2]/div/a[2]')
	we.click()
	driver.implicitly_wait(10)
	video =driver.find_element_by_xpath('//*[@id="playerContainer"]/div[4]/span/span[2]')
	video.click()
	print("Test Succesfull")
	