import sys
file_name = sys.argv[1]

html_head = "<html><body><table>"
html_footer= "</table></body></html>"

wf=open("html_file.html","w") 
try:
	fh=open(file_name,"r")
except:
	print "not opening file"
else:
	for line in fh:
		html_head=html_head+"<tr>"
		line = line.rstrip("\n")
		data = line.split(",")
		for i in data:
			html_head=html_head+"<td>"+i+"</td>"
		html_head=html_head+"<tr>"
	html_head=html_head+html_footer
	fh.close()
	wf.write(html_head)
	wf.close()


