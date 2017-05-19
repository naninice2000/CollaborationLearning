import sys

file_name = sys.argv[1]

line_list = open(file_name,"r")
for line in line_list:
	line = line.rstrip("\n")
	data = line.split(",")
	print data[0],data[1],data[2],data[3],data[4]
line_list.close()
