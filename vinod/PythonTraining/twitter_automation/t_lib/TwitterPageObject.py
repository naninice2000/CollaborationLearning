class HomePageObjectModel:

	def __init__(self):
		pass


	def get_login_button_we(self):
		return "//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[3]"

	def get_login_message_after_click(self):
		return "login-dialog-header"
		

	def get_signup_button_we(self):
		return "//*[@id=\"doc\"]/div[1]/div/div[1]/div[2]/a[2]"

	def get_signup_button_click(self):
		return "//*[@id=\"page-container\"]/div/div/h1"


