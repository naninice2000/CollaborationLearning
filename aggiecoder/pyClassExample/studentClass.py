class student:
	student_fname = "" 
	student_lname = ""
	student_ID = ""
	student_email = ""
	student_phone_num = ""
	student_major = ""
	student_minor = ""
	student_classification = ""
	
	#initialization
	def __init__(self):
		print" Student Profile Created "
	
	#setfunctions
	def setStudentFullName(self,fname,lname):
		self.student_fname = fname
		self.student_lname = lname

	def setStudentID(self, ID):
		self.student_ID = ID

	def setStudentEmail(self, Email):
		self.student_email = Email
	
	def setStudentPhoneNumber(self, Number):
		self.student_phone_num = Number

	def setStudentMajor(self, Major):
		self.student_major = Major
	
	def setStudentMinor(self, Minor):
		self.student_minor = Minor
	
	def setStudentClassification(self, Classification):
		self.student_classification = Classification
	
	#getfunctions
	def getStudentFullName(self):
		full_name = self.student_fname + " " + self.student_lname
		return full_name

	def getStudentID(self):
		studentID = self.student_ID
		return studentID
	
	def getStudentEmail(self):
		studentEmail = 	self.setStudentEmail
		return studentEmail
	
	def getStudentPhoneNumber(self):
		phoneNumber = self.student_phone_num 
		return phoneNumber
	
	def getStudentMajor (self):
		studentMajor = 	self.student_major
		return studentMajor

	def getStudentMinor (self):
		studentMinor = 	self.student_minor 
		return studentMinor
	
	def getStudentClassification(self):
		studentClassification = self.setStudentClassification 
		return studentClassification
	





	