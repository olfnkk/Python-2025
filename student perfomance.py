import csv

with open('student_performance.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    data = list(reader)

for row in data:
    row['total_score'] = float(row['total_score'].replace(',', '.'))

for i in range(len(data)):
    min_index = i
    for j in range(i + 1, len(data)):
        if data[j]['total_score'] < data[min_index]['total_score']:
            min_index = j
    data[i], data[min_index] = data[min_index], data[i]

print("Відсортовані дані (за total_score):")
for row in data:
    print(f"{row['total_score']};{row['grade']}")