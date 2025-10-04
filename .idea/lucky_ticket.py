num = input(("Введите номер билета: "))
print("Счастливый билет" if sum(map(int, num[:3])) == sum(map(int, num[3:])) else "Несчастливый билет")
