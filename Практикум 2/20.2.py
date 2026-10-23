kletka = input()
bykva = kletka[0]
number = int(kletka[1])
bykva_v_number = ord(bykva) - 96
total = bykva_v_number + number
if total % 2 == 0:
    print("черный")
else:
    print("белый")