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

	def get_username_input_we(self):
		return"session[username_or_email]"

	def get_passw_button_we(self):
		return"session[password]"
		

	def get_login_loginpage(self):
		return"//*[@id=\"page-container\"]/div/div[1]/form/div[2]/button"
	
	def get_invalide_credentials_message(self):
		return"//*[@id=\"message-drawer\"]/div/div/span"

#<button type="submit" class="submit EdgeButton EdgeButton--primary EdgeButtom--medium">Log in</button>


