from selenium import webdriver
import pytest

chromedriver_path = "C:\Users\johns\Downloads\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(chromedriver_path)
driver.get("http://facebook.com")
'''
we_login =driver.find_element_by_xpath("//*[@id=\"u_0_y\"]")
we_login.click()
'''

driver.implicitly_wait(10)
email_id = driver.find_element_by_xpath("//*[@id=\"email\"]")
#email_id = driver.find_element_by_name("username_or_email")
email_id.send_keys("johnsonrokati@gmail.com")
password = driver.find_element_by_xpath("//*[@id=\"pass\"]")
password.send_keys("johnson@2103")
we_login1 =driver.find_element_by_xpath("//*[@id=\"u_0_q\"]")
we_login1.click()
driver.implicitly_wait(10)
