n=raw_input("enter no of rows")
n=int(n)
for i in range(0,n):
    a=""
    for j in range(0,n-i-1):
         a=a+" "
    for j in range(0,i+1):
        a=a+"* "
    
    print a

