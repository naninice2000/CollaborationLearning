from selenium import webdriver
import pytest 

chromedriver_path = "C:/Users/shrut/Documents/GitHub/CollaborationLearning/vinod/PythonTraining/chromedriver_win32/chromedriver.exe"
'''
def testCheckLandingPageTitle():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	assert "Twitter. It's what's happening" in driver.title
	driver.quit()


def testSingupButton():
 driver = webdriver.Chrome(chromedriver_path)
 driver.get("http://twitter.com")
 we = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[2]")
 print we.text
 driver.quit()

# verrify sign up will take to next page
def testSingupButton():

 	driver = webdriver.Chrome(chromedriver_path)
 	driver.get("http://twitter.com")
 	we = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[2]")
 	we.click()
 	driver.implicitly_wait(10)
 	full_name_we = driver.find_element_by_id("full-name")
 	full_name_we.send_keys("Venkat Ram")
 	#driver.implicitly_wait(10)
	email_id = driver.find_element_by_id("email")
	email_id.send_keys("ad23456778@gmail.com")
	password = driver.find_element_by_id("password")
	password.send_keys("anilbeesu")
	we_sign =driver.find_element_by_xpath("//*[@id=\"phx-signup-form\"]/div[3]/div")
	we_sign.click()
	next_page = driver.find_element_by_xpath("//*[@id=\"page-container\"]/div/div/h1")
	print next_page.text
	assert next_page.text in "Enter your phone."


# verify  error message when you enter blank space in name feild
def testName_feild_error():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	click_singup = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[2]")
 	click_singup.click()
 	driver.implicitly_wait(10)
 	full_name_we = driver.find_element_by_id("full-name")
 	full_name_we.send_keys("   ")
 	error_message = driver.find_element_by_xpath("//*[@id=\"phx-signup-form\"]/div[1]/div[1]/div/div/p[2]")
 	print error_message.text
 	assert error_message.text in "What's your name?"
 	driver.quit()

#verify error message in email id 
def testemailid_error():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	click_singup = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[2]")
 	click_singup.click()
 	driver.implicitly_wait(10)
 	email_id_error = driver.find_element_by_id("email")
 	email_id_error.send_keys(" d.d  ")
 	error_message = driver.find_element_by_xpath("//*[@id=\"phx-signup-form\"]/div[1]/div[2]/div/div[1]/p[3]")
 	print error_message.text
 	assert error_message.text in "Please enter a valid email."
 	driver.quit()

#verify error message in password feild
def testpassword_error():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	click_singup = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[2]")
 	click_singup.click()
 	driver.implicitly_wait(10)
 	password = driver.find_element_by_id("password")
	password.send_keys("anil")
 	error_message = driver.find_element_by_xpath("//*[@id=\"phx-signup-form\"]/div[1]/div[3]/div[1]/div/p[4]")
 	print error_message.text
 	assert error_message.text in "Your password must be at least 6 characters."
 	driver.quit()

 	

 
# verify login details when crdentials not matched
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
	error_message = driver.find_element_by_xpath("//*[@id=\"message-drawer\"]/div/div/span")
	print error_message.text
	assert error_message.text in "The email and password you entered did not match our records. Please double-check and try again."

# verify forgot password  button 
def test_forgotpassword_button():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	we_login =driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[3]")
	we_login.click()
	driver.implicitly_wait(10)
	content = driver.find_element_by_class_name("forgot")
	content.click()
	driver.implicitly_wait(10)
	navigate_next_page = driver.find_element_by_class_name('PageHeader')

	print navigate_next_page.text
	assert navigate_next_page.text in "Find your Twitter account"



#Verify message by  not entering any thing in login button detail
def testBlanksigninbutton():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	sign3 =driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[3]")
	sign3.click()
	driver.implicitly_wait(10)
	we_sign1 =driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/input[1]")
	we_sign1.click()
	error_message =driver.find_element_by_xpath("//*[@id=\"message-drawer\"]/div/div/span")
	print error_message.text
	assert error_message.text in "The username and password you entered did not match our records. Please double-check and try again." 

def test_activate_button():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	sign3 =driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[3]")
	sign3.click()
	driver.implicitly_wait(10)
	signup = driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/input[1]")
	signup.click()
	driver.implicitly_wait(10)

	activate = driver.find_element_by_xpath("//*[@id=\"page-container\"]/div/div[2]/p[2]/a")
	activate.click()
	display_message = driver.find_element_by_tag_name("h1")
	print display_message.text
	assert display_message.text in "Sign up to use Twitter on the web."
'''

def test_activate_by_invalidphone():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")
	sign3 =driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[3]")
	sign3.click()
	driver.implicitly_wait(10)
	signup = driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/input[1]")
	signup.click()
	driver.implicitly_wait(10)

	activate = driver.find_element_by_xpath("//*[@id=\"page-container\"]/div/div[2]/p[2]/a")
	activate.click()

	address = driver.find_element_by_id("address")
	address.send_keys("248")
	submit = driver.find_element_by_class_name("submit")
	print submit.text

	assert submit.text in "We couldn't find that number. Please try again."


	






'''def testfeaturebutton():
	driver = webdriver.Chrome(chromedriver_path)
	driver.get("http://twitter.com")

	feature = driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[2]/div/a[1]/span")
	feature.click()'''
//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[2]






