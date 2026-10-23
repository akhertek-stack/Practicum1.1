import math
doroshka = input()
a, b = map(float, doroshka.split('x'))
r = 6.5
diagonal_doroshki = math.sqrt(a**2 + b**2) / 2
if diagonal_doroshki <= r:
    print("да")
else:
    print("нет")