kirill, Arina, Sergey = map(int, input().split())
if kirill >= Arina and kirill >= Sergey:
    print(kirill)
elif Arina >= kirill and Arina >= Sergey:
    print(Arina)
else:
    print(Sergey)