# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num, summ = input('Введите число: '), 0
num = num.replace('-', '')
num = num.replace(',', '')
num = num.replace('.', '')
for i in range(len(num)):
    summ += int(num[i])
print(summ)
