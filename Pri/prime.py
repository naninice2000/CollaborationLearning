a=3
b=100
print("prime numbers between",a,"and",b,"are:")

for i in range(a,b+1):
	if i>1:
		for j in range(2,i):
			if(i%j==0):
				break
		else:
			print i