import sys
file_name = sys.argv[1]

header = "<html>,<body>,<table border = 1>"
footer = "</table>,</body>,</html>"

htmlfile = open("htmlfile.html","w") 

try:
	line_list=open(file_name,"r")
	
except:
	print "file does not exist", file_name
	
else:
	for line in line_list:
		header = header + "<tr>"
		line= line.rstrip("\n")
		data = line.split(",")
		for i in data:
			header = header + "<td>"+i+"</td>"
		header = header +"</tr>"		
	header = header + footer 
	line_list.close()
	htmlfile.write(header)
	htmlfile.close()