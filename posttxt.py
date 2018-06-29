#handling person by person data

import re

import xlsxwriter
workbook=xlsxwriter.Workbook('memberslist.xlsx')
worksheet=workbook.add_worksheet()
worksheet.write(0,0,'Name')
worksheet.write(0,1,'Cell Number')
worksheet.write(0,2,'E-Mail ID')
worksheet.write(0,3,'DOB')
worksheet.write(0,4,'Mem_ID')
worksheet.write(0,5,'City')
worksheet.write(0,6,'Fax Number')
worksheet.write(0,7,'Tele Number')
worksheet.write(0,8,'Resi Number')


per_person = open('re_new.txt','r')

block_index=[]
block_text=[]

n=0
for i,line in enumerate(per_person):
	if line.startswith('\n'):
		block_index.append(n)
	n=n+1

# print(block_index)
# print(range(len(block_index)-1))
per_person.close()

per_person = open('re_new.txt','r')

only_lines = per_person.readlines()

for j in list(range(len(block_index))):
	if j==(len(block_index)-1):
		lastline = len(only_lines)
	else:
		lastline = block_index[j+1]

	for k in range(block_index[j]+1,lastline):
		only_lines[k]=only_lines[k].rstrip()
		only_lines[k] = unicode(only_lines[k], errors='ignore')
# 		print(only_lines[k])

		#separate name
# 		name_ind = (only_lines[k].find('ACS') or only_lines[k].find('FCS'))
# # 		print(name_ind)
# 		if name_ind !=-1:
# 			name = only_lines[k][:name_ind]
# 			print(name)

		#separate name(column 0) and mem_id(column 4)
		if (only_lines[k].find('ACS')!=-1):
			name_ind = only_lines[k].find('ACS')
			name = only_lines[k][:name_ind]
			mem_id = only_lines[k][name_ind:]
			worksheet.write(j+1,0,name)
			worksheet.write(j+1,4,mem_id)
		elif (only_lines[k].find('FCS')!=-1):
			name_ind = only_lines[k].find('FCS')
			name = only_lines[k][:name_ind]
			mem_id = only_lines[k][name_ind:]
# 			print(mem_id)
# 			print(name)
			worksheet.write(j+1,0,name)
			worksheet.write(j+1,4,mem_id)

		#separate cell number(column 1)
		cell_num_ind = only_lines[k].find('CELL-')
		if cell_num_ind!=-1:
			cell_number = only_lines[k][cell_num_ind+5:]
# 			print(number)
			worksheet.write(j+1,1,cell_number)

# 		separate fax number(column 6)
		fax_num_ind = only_lines[k].find('FAX-')
		if fax_num_ind!=-1:
			fax_number = only_lines[k][fax_num_ind+4:]
# 			print(fax_number)
			worksheet.write(j+1,6,fax_number)

		#separate tele number(column 7)
		tele_num_ind = only_lines[k].find(' T-')
		if tele_num_ind!=-1:
			tele_number = only_lines[k][tele_num_ind+3:]
# 			print(tele_number)
			worksheet.write(j+1,7,tele_number)

		#separate Resi number(column 8)
		resi_num_ind = only_lines[k].find(' R-')
# 		resi_num_ind_2 = re.findall('^R-',only_lines[k])
		if resi_num_ind!=-1:
			resi_number = only_lines[k][resi_num_ind+3:]
# 			print(resi_number)
# 		print(resi_num_ind_2)
			worksheet.write(j+1,8,resi_number)

		#separate email address (columne 2)
		email_index = only_lines[k].find('E-Mail:')
		if email_index!=-1:
			email_name = only_lines[k][email_index+7:]
# 			print(email_name)

		#separate domain name ... cont. email
		domain_index = only_lines[k].find('@')
		if domain_index!=-1:
			mail_domain = only_lines[k][domain_index:]
# 			print(mail_domain)
			email_id = email_name+mail_domain
# 			print(email_id)
			worksheet.write(j+1,2,email_id)

		#separate date of birth (column 3)
		dob_ind = re.findall('(\d+\-\d+\-\d{4})',only_lines[k])
		if len(dob_ind)>0:
# 			dob=only_lines[k][dob_ind+2:]
# 			print(dob_ind)
			worksheet.write(j+1,3,dob_ind[0])

		#separate City (column 5)
		city_ind=re.findall('(^[A-Z]+\-\d{6})',only_lines[k])
		if len(city_ind)>0:
			city_name = city_ind[0].partition('-')[0]
			if len(city_name)>=3:
# 				print(city_name)
				worksheet.write(j+1,5,city_name)

# 	print('\n')

workbook.close()

# 		block_text.append(only_lines[k])
