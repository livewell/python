#pylint: skip-file

import csv

fileName = open('sample.csv')
csv_f = csv.reader(fileName)

countyName = []

for row in csv_f:
    countyName.append(row[2])
   
print (*countyName, sep='\n')