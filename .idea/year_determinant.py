year = int(input("Введите год: "))
print("Результат: " + (" високосный год" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else " год не високосный"))