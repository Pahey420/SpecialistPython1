# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

with open("data/info.txt", "r") as f:
    positive_number = 0
    negative_counter = 0
    negative_number = 0
    for positive_counter in f:
        positive_counter = positive_counter.strip()  # удаляем все лишние переносы строк
        if positive_counter.isnumeric():
            positive_number += int(positive_counter)
            # print(positive_number)   # вывести положительное число
    f.seek(0)
    for negative_counter in f:
        negative_counter = negative_counter.strip()
        if negative_counter.find("-") == 0:
            negative_counter = negative_counter.replace("-", "")
            if negative_counter.isdecimal():
                negative_number += int(negative_counter)
    # print(negative_number)     # вывести положительное от отрицального число
print("totl: ", positive_number - negative_number)
pass
