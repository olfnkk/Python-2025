# ================================
# Домашнє завдання: Основи Python
# ================================

# 1. Print та input
# Напишіть програму, яка запитує ім'я користувача
# та виводить повідомлення "Hello, <ім'я>!"
print(f"Hello, {input("Please, write your name")}!")




# 2. Арифметика
# Запросіть два числа від користувача.
# Виведіть результат: додавання, віднімання, множення, ділення (/ та //),
# залишок від ділення (%) та піднесення до степеня (**).
num1=int(input("Please, write a number: "))
num2=int(input("Please, write another number: "))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)
print(num1%num2)
print(num1**num2)



# 3. Типи даних
# Запросіть будь-яке число від користувача (input).
# Виведіть його тип. Потім перетворіть у int та float і знову виведіть типи.
num=input("Write a number: ")
print(type(num))
print(int(num))
print(float(num))


# 4. Умовні оператори
# Запросіть два числа a і b.
# Якщо a > b, виведіть "a більше за b".
# Якщо a == b, виведіть "a дорівнює b".
# Інакше виведіть "a менше за b".
a=int(input("a = "))
b=int(input("b = "))
if a>b:
    print("a більше за b")
elif a==b:
    print("a дорівнює b")
else:
   print("a менше за b")


# 5. Парність числа
# Запросіть число у користувача і перевірте, чи воно парне чи непарне.
#Використайте оператор %.
n=int(input('Enter a number: '))
if n%2==0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')

# 6. Match / Case
# Запросіть число від 1 до 7.
# Використайте конструкцію match/case, щоб вивести:
# 1–5 → "Weekday"
# 6–7 → "Weekend"
# інше → "Invalid day"
number=int(input('Enter a number from 1 to 7: '))
match number:
    case 1 | 2 | 3 | 4 | 5 :
        print("Weekday")
    case 6 | 7 :
        print("Weekend")
    case _:
        print("Invalid day")

# 7. Додаткове
# Запитайте код відповіді сервера (200, 404, 500).
# Використайте match/case, щоб вивести:
# 200 → "OK"
# 404 → "Not Found"
# 500 → "Server Error"
# інші → "Unknown"
code=int(input("Enter code: "))
match code:
     case 200:
         print("OK")
     case 404:
         print("Not Found")
     case 500:
         print("Server Error")
     case _:
         print("Unknown")


# 8. Створіть функцію hello(), яка запитує ім'я користувача (input)
#    і виводить "Hello, <ім'я>!"
def say_hello():
    name=input('Enter your name: ')
    print(f'Hello {name}')
say_hello()



# 9. Створіть функцію add(a, b), яка повертає суму двох чисел.
#    Запросіть два числа у користувача та виведіть результат через цю функцію.
def add(a, b):
    return(a+b)
a=int(input("a="))
b=int(input("b="))
print(add(a, b))

# 10. Створіть функцію is_even(n), яка повертає True, якщо число парне,
#    і False, якщо непарне. Перевірте цю функцію на кількох прикладах.
def is_even(n):
    if n % 2 == 0:
        return True
    else:
       return False
print(is_even(int(input("Enter a number: "))))



# 11. Створіть функцію max_of_three(a, b, c), яка повертає найбільше з трьох чисел.
#    Запросіть три числа у користувача та виведіть результат.
def max_of_three(a, b, c):
    return max(a, b, c)
print(max_of_three(int(input("first number=")), int(input("second number=")), int(input("third number="))))


# 12.Створіть функцію factorial(n), яка обчислює факторіал числа n.
#    Поясніть різницю між return і print у функції.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result=result*i
    return result

num = int(input("Введіть число: "))
print("Факторіал:", factorial(num))
