import json


class ConfigReader:
	config_file = ""
	config_map = {}

	def __init__(self):
		self.config_file = conf_file
		with open(self.config_file) as data_file:    
			self.config_map = json.load(data_file)
			
	
	def get_test_environment_details(self):
		return self.config_map
        
