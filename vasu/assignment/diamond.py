n = int(input("Enter the size: "))

for i in range(n-1):
    print((n-i) * ' ' + (2*i+1) * '*')
for i in range(n-1, -1, -1):
    print((n-i) * ' ' + (2*i+1) * '*')
	
	
	