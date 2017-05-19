import sys

file_name = sys.argv[1]
head = '<html>'
body = '<body>'
line_list=open(file_name,"r")
htmlfile = open("htmlfile.html","w") 
htmlfile.write(head)
htmlfile.write(body)
htmlfile.write('<table>')
for line in line_list:
		line = line.rstrip("\n")
		data = line.split(",")
		htmlfile.write( '<td>', data[0], data[1], data[2], data[3], data[4], '</td>')
htmlfile.write ( '<td>')
htmlfile.write ('</table>')
line_list.close()
htmlfile.close()