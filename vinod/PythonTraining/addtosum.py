a=1
s=0
print("enter number to add toy the sum.")
print("enter 0 to quit.")
while a!=0:
	print("current sum",s)
	a=float(input("number?"))
	a=float(a)
	s += a
print("total sum",s)