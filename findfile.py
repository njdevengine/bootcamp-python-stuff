import os

#import a package to read in csv

import csv

#create the path for the file
#same as path = '../Resources/accounting.csv
csvpath = os.path.join('..','Resources','accounting.csv')
print(csvpath)
	with open(csvpath, 'r') as fileHandle:
		lines=fileHandle.read()
		print(lines)
		
with open(csvpath, newline='') as casfileH:
	csvReader =csv.reader(casfileH, delimiter=',')
	print(csvReader)
