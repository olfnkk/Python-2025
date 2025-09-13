# Завдання 1
# Створіть список із 5 чисел. Виведіть суму всіх елементів.
sum=0
list=[1,2,3,4,5]
for i in list:
    sum+=i
print(sum)

# Завдання 2
# Користувач вводить 5 чисел. Збережіть їх у список та виведіть найбільше число.
l=[0]
for i in range(5):
   num=int(input("Enter a number: "))
   l.append(num)
print(max(l))

# Завдання 3
# Є список ["apple", "banana", "cherry"].
# Додайте до нього "orange" і видаліть "banana".
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("banana")
print(fruits)

# Завдання 4
# Є список чисел. Виведіть тільки ті числа, які діляться на 2.
numbers=[1,6,7,4,7,4,45]
n=[]
for number in numbers:
    if number%2==0:
        n.append(number)
    else:
        continue
print(n)


# Завдання 5
# Є кортеж (10, 20, 30, 40).
# Виведіть перший і останній елемент.
point=(10, 20, 30, 40)
print(point[0])
print(point[-1])

# Завдання 6
# Є два множини: {1,2,3,4} і {3,4,5,6}.
# Знайдіть їх об’єднання, перетин і різницю.
a={1,2,3,4}
b={3,4,5,6}
print(a | b)
print(a & b)
print(a - b)


# Завдання 7
# Користувач вводить рядок.
# Зробіть з нього множину символів (щоб лишилися тільки унікальні символи).
new=input("Enter smth: ")
print(set(new))

# Завдання 8
# Є словник {"name":"Ivan","age":20,"group":"251EC"}.
# Виведіть усі ключі і значення в циклі.
student = {"name": "Ivan", "age": 20, "group": "251EC"}
for key, value in student.items():
    print(f"{key}: {value}")


# Завдання 9
# Створіть словник оцінок студентів: {"Ivan":90, "Petro":75, "Olga":100}.
# Знайдіть середню оцінку.
grades=0
students={"Ivan":90, "Petro":75, "Olga":100}
for key, value in students.items():
    grades+=value
print(grades)

# Завдання 10
# Користувач вводить слова через пробіл.
# Збережіть їх у список і підрахуйте, скільки разів зустрічається кожне слово.
# Користувач вводить слова через пробіл
text = input("Please, write words: ")
word_list = text.split()
word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for w, c in word_count.items():
    print(f"{w}: {c}")


