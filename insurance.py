import csv

with open('insurance.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

for row in data:
    row['charges'] = float(row['charges'])

n = len(data)
for i in range(n - 1):
    for j in range(n - i - 1):
        if data[j]['charges'] > data[j + 1]['charges']:
            data[j], data[j + 1] = data[j + 1], data[j]

for row in data:
    print(row)

