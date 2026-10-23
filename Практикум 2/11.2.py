import math

# Считываем данные по порядку, как в примерах на скриншоте
xc = float(input())
yc = float(input())
r = float(input())
x = float(input())
y = float(input())
distance = math.sqrt((x - xc)**2 + (y - yc)**2)
if distance < r:
    print("Точка внутри окружности")
elif distance == r:
    print("Точка лежит на окружности")
else:
    print("Точка за пределами окружности")