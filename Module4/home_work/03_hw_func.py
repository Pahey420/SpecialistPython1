# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here
x1 = 13
y1 = 12
x2 = 10
y2 = 12
R1 = 4
R2 = 4
def distance(x1, y1, x2, y2):
    # TODO: тело, которое вы реализовали на практической работе
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("окружность целиком внутри другой: ", (R2-R1)**2 > (x2-x1)**2 + (y2-y1)**2) # найденное решение, пояснить не могу
print("окружность целиком внутри другой: ", distance(x1, y1, x2, y2) + R1 >= R2 or distance(x1, y1, x2, y2) + R2 >= R1) # если не важно кокая окружность в какую вписана
print("окружность целиком внутри другой: ", distance(x1, y1, x2, y2) + R1 > R2) # если в по условию R2 пытаемся вписать в R1, при этом окружности не идентичны
print("окружность целиком внутри другой: ", distance(x1, y1, x2, y2) + R1 >= R2) # если в по условию R2 пытаемся вписать в R1, при этом окружности идентичны
