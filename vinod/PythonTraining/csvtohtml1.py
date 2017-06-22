import sys
file_name=sys.argv[1]
html_head ="<html><body><table border = 1>"
html_footer ="</table></body></html>"
a=open("csvhtml.html","w")
try:
	b=open(file_name,"r")
except:
	print"not able to open"
else:
	for line in b:
		html_head=html_head+"<tr>"
		line =line.rstrip("\n")
		data=line.split(",")
		for i in data:
			html_head=html_head+"<td>"+i+"</td>"
		html_head=html_head+"</tr>"
	html_head=html_head+html_footer
	b.close()
	a.write(html_head)
	a.close()