import pytest

class TestTwitterHomePage:
	
	chromedriver_path = "../lib/chromedriver.exe"
	driver = webdriver.Chrome(chromedriver_path)
	
	def test_home_page_title(self):
		self.driver.get("http://twitter.com")
		assert self.driver.title = "Twitter. It's what's happening."