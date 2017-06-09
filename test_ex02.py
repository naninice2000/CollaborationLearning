from selenium import webdriver
import pytest

chromedriver_path = "C:\Users\johns\Downloads\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(chromedriver_path)
driver.get("http://twitter.com")
we_login =driver.find_element_by_xpath("//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[3]")
we_login.click()

driver.implicitly_wait(10)
email_id = driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/div[1]/input")
#email_id = driver.find_element_by_name("username_or_email")
email_id.send_keys("xyz@gmail.com")
password = driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/div[2]/input")
password.send_keys("*********")
we_login1 =driver.find_element_by_xpath("//*[@id=\"login-dialog-dialog\"]/div[2]/div[2]/div[2]/form/input[1]")
we_login1.click()
driver.implicitly_wait(10)



