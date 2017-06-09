from studentClass import student
print "Let's Create your Student Profile"
print " "
fname = raw_input(" Enter First Name: " )
lname = raw_input(" Enter Last Name: " )
ID = raw_input(" Enter ID Number: ")
Email_Address = raw_input(" Enter Email Address: ")
Number = raw_input(" Enter Phone Number: ")
Major = raw_input(" Enter Major: ")
Minor = raw_input(" Enter Minor: ")
Class = raw_input(" Enter Class: ")

Student_id = int(ID)
Student_Number = int(Number)
student_obj = student()
student_obj.setStudentFullName(fname,lname)
student_obj.setStudentID(Student_id)
student_obj.setStudentEmail(Email_Address)
student_obj.setStudentPhoneNumber(Student_Number)
student_obj.setStudentMajor(Major)
student_obj.setStudentMinor(Minor)
student_obj.setStudentClassification(Class)

print "\n"
print "Student Name: " 
print student_obj.getStudentFullName()
print "\n"
print  "Student ID: " 
print student_obj.getStudentID()
print "\n"
print "Student Email: " 
print student_obj.getStudentEmail()
print "\n"
print "Student Phone Number: " 
print student_obj.getStudentPhoneNumber()
print "\n"
print "Student Major " 
print student_obj.getStudentMajor()
print "\n"
print "Student Minor: " 
print student_obj.getStudentMinor()
print "\n"
print "Student Class: " 
print student_obj.getStudentClassification()
print "\n"





