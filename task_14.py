#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

n = int(input("Введите число: "))

power_of_two = 1
while power_of_two <= n:
    print(power_of_two, end=", ")
    power_of_two *= 2