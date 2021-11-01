import csv

file = open('converted2.csv')
csvreader = csv.reader(file)

rows = []
for row in csvreader:
    rows.append(row)
print(rows)