import csv

def detect_delimiter(filename):
    with open(filename, encoding="utf-8-sig") as file:
        sample = file.readline()
        if ";" in sample:
            return ";"
        elif "\t" in sample:
            return "\t"
        else:
            return ","


def load_names(filename):
    delimiter = detect_delimiter(filename)
    with open(filename, encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        names = [row["Name"].strip() for row in reader if row.get("Name")]
    return names


def linear_search(data, target):
    for i, name in enumerate(data):
        if name.lower() == target.lower():
            return i
    return -1


def binary_search(sorted_data, target):
    left, right = 0, len(sorted_data) - 1
    target = target.lower()
    while left <= right:
        mid = (left + right) // 2
        name = sorted_data[mid].lower()
        if name == target:
            return mid
        elif name < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


filename = "name_gender_dataset.csv"
names = load_names(filename)
target_name = input("Введіть ім’я для пошуку: ").strip()


index_linear = linear_search(names, target_name)
if index_linear != -1:
    print(f"Ім’я '{target_name}' знайдено (лінійний пошук, позиція {index_linear})")
else:
    print(f"Ім’я '{target_name}' не знайдено (лінійний пошук)")


names.sort()
index_binary = binary_search(names, target_name)
if index_binary != -1:
    print(f"Ім’я '{target_name}' знайдено (бінарний пошук, позиція {index_binary})")
else:
    print(f"Ім’я '{target_name}' не знайдено (бінарний пошук)")
