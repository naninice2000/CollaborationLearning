n=20
for number in range(0,n):
	if number>1:
		for i in range(2,number):
			if(number%i)==0:
				break
		else:
			print number
		
