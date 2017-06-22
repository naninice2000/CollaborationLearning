import sys

class HomePageObjectModel:
	def __init__(self):
		pass
	def get_login_button_we(self):
		return "//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[3]"
	def get_signup_button_we(self):
		return "//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[2]"
	def get_sports_button_we(self):
		return "//*[@id=\"doc\"]/div[1]/div/div[2]/div/a[2]/span"