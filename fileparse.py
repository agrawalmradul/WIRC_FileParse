#pdf parsing for first page

print ("hello world")

import PyPDF2

pdffile = open('listmem.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdffile)
# range_pages = pdfReader.numPages

pageObj = pdfReader.getPage(0)
extracted_text = pageObj.extractText()

out_file = open('out_txt.txt','w') 
out_file.write(extracted_text)
out_file.close()

rewrite_file = open('rewrite.txt','w')
reread_file=open('out_txt.txt','r')
for line in reread_file:
	if line.startswith(' '):
		line = line.lstrip()
	if line.startswith('\n'):
		line = line.rstrip()
	rewrite_file.write(line)
rewrite_file.close()

#######################
#This block will separate per-person data
#######################
data_proc = open('rewrite.txt','r')
prevLine=''
# print(enumerate(data_proc))
write_file = open('re_new.txt','w')

for line in data_proc:
	if (line.find('ACS')!=-1) or (line.find('FCS')!=-1):
		prevLine = (prevLine+'\n')
	write_file.write(prevLine)
	prevLine=line
write_file.write(line)	
write_file.close()