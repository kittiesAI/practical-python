# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    total_cost = 0
    for line in f:
        row = line.split(',')
        total_cost = total_cost + int(row[1]) * float(row[2])
    
print('Total cost', total_cost)


# With zipped files, the file is stored as byte string
# So we need to convert it into text string with .decode('utf-8')
total_cost_zipped = 0
import gzip
with gzip.open('Data/portfolio.csv.gz') as f:
    headers = next(f)
    for line in f:
        line = line.decode('utf-8')
        row = line.split(',')
        total_cost_zipped = total_cost_zipped + int(row[1]) * float(row[2])
        
print('Zipped file: Total cost', total_cost_zipped)