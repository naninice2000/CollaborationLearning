while True:
	print("enter '0' for exit ")
	num=raw_input("enter the required multiplcation table : ")
	num=int(num)
	print"Multiplication Table"
        print"--------------------"
	if num==0:
		break
	else:
		for i in range(1,11):
			print (num,"*",i,"=",num*i)
