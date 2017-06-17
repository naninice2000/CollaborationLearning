import json	

class employee: 

	def __init__(self,name):
		self.name = name
	
f=open("employee_confi.txt","r")
s=f.read()
#print(s)
employee=json.loads(s)
#print (employee)
#print employee ("nikhil")
for person in (employee):
	print(employee[person])
	print type (employee)
	
	