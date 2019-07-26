import sys
import pandas as pd
import xlrd
import csv

dict1 = { 'client_id':'',
		'agency_id':'',
		'cli_ref'  :'',
		'name1'    :'',
		'balance'  :'',
		'addr1'    :'',
		'addr2'    :'',
		'city1'    :'',
		'state1'   :'',
		'zip1'     :'',
		'country1' :'',
		'inv_num'  :'',
		'inv_date' :'',
		'phone1'   :'',
		'phone2'   :'',
		'name2'    :'',
		'email1'   :'',
		'misc1'    :'',
		'misc2'    :'',
		'misc3'    :'',
		'misc4'    :''}

xls = pd.ExcelFile(sys.argv[1])
sheet1 = xls.parse(0)

client_id = '{}'.format(str(raw_input('client_id = ')))
agency_id = sheet1['Currency']
cli_ref = sheet1['Payer']
name1 = sheet1['Name 1']
balance = sheet1['Due Amount']
addr1 = sheet1['Address']
city1 = sheet1['Location']
zip1 = sheet1['Postal Code']
country1 = sheet1['Country']
phone1 = sheet1['Telephone']
inv_num = sheet1['Doc.number']
inv_date = sheet1['Document Date']


misc1 = sheet1['Company code']
misc2 = sheet1['Company code Name']
misc3 = sheet1['Vat Number']
email1 = sheet1['Email']

with open('placement.csv', 'r') as readFile:
	reader = csv.reader(readFile)
	lines = list(reader)

del lines[1:]

with open('placement.csv', 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerow(dict1.keys())

no_inv = len(cli_ref)

for i in range(no_inv):
	dict1['client_id'] = client_id
	dict1['agency_id'] = agency_id[i]
	dict1['cli_ref'] = cli_ref[i]
	dict1['name1'] = name1[i]
	dict1['balance'] = balance[i]
	dict1['addr1'] = addr1[i]
	dict1['city1'] = city1[i]
	dict1['zip1'] = zip1[i]
	dict1['country1'] = country1[i]
	dict1['phone1'] = phone1[i]
	dict1['inv_num'] = inv_num[i]
	dict1['inv_date'] = inv_date[i]
	dict1['email1'] = email1[i]
	dict1['misc1'] = misc1[i]
	dict1['misc2'] = misc2[i]
	dict1['misc3'] = misc3[i]

	data = dict1.values()

	with open('placement.csv', 'a') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(data)

readFile.close()
writeFile.close()
csvFile.close()

