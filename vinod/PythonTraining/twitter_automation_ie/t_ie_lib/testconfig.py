import json

class TestConfig: 
	config_file = ""
	config_map = {}

	def __init__(self,conf_file):
		self.config_file = conf_file

	def readConfig(self):
		with open(self.config_file) as data_file:    
			self.config_map = json.load(data_file)

	def getConfig(self,env):
		return self.config_map[env]

	def getPortocolInfo(self,env):
		return self.config_map[env]["url"]

	def getPortalIP(self,env):
		return self.config_map[env]["protocol"]

	#def getPortInfo(self,env):
		#return self.config_map[env]["port"]
	#def __init__(self,protocol,ip,port):
			#self.url = protocol+"://"+ip+":"+port+"/"
			#self.s = requests.Session()