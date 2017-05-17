odd=raw_input("Enter the number to get odd number :")
odd=int(odd)
print "Below list are odd number"
print"----------------------------"
for i in range(1,odd):
	if(i%2==1):
		print i
