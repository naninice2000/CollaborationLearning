import os 
from selenium import webdriver

chromedriver_path = "C:\Users\johns\Downloads\chromedriver_win32\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver_path
driver = webdriver.Chrome(chromedriver_path)
driver.get("http://twitter.com")
