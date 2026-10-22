x, y, n = map(int, input().split())

dohod = (x * 100 + y) * n
rub = dohod // 100
kop = dohod % 100

print(f"{rub} руб. {kop} коп.")