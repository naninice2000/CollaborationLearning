import sys

file_list = sys.argv[1]


html_head = "<html><body><tables>"
html_footer = "</tables><body></html>"



line_list = open (file_list, "r")
for line in line_list:
	line=line.rstrip("\n")
	data=line.split(",")
 	print data[0], data[1], data[2], data[3]
line_list.close()