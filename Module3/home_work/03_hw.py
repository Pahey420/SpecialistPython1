# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
numbers = ['2', '-4', '5', '0', '-7', '4', '2']
count = []
for number in numbers:
    number = int(number)
    num = 0
    if number > 0 and number % 2 == 0:
        num += number
        count.append(num)
num = int(num)
print(sum(count))
