#!  /usr/bin/python

import sys
file_name=sys.argv[1]

head = "<html><body><table border=6 bordercolor=purple>"
footer= "</table></body></html>"

wf=open("html_table.html","w")
try:
  fh=open(file_name,"r")
except:
  print "unable to open"
else:
  for line in fh:
    head=head+"<tr>"
    line=line.rstrip("\n")
    data=line.split(",")
    for i in data:
      head=head+"<td>"+i+"</td>"
    head=head+"</tr>"
  head=head+footer
  fh.close()
  wf.write(head)
  wf.close()
