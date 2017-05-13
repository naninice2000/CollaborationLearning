x= raw_input("please enter the number of rows")
x= int(x)

for i in range(1, x+1):
	a= ""

	for j in range(0,i):
		a= a+"* "
	for k in range(0,x-i):
		a= a+"  "
	print a
