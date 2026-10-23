num = int(input())
chislo1 = num // 1000
chislo2 = (num % 1000)// 100
chislo3 = (num % 100) // 10
chislo4 = num % 10
if chislo1 == chislo4 and chislo3 == chislo2:
    print("настоящее")
else:
    print("кривое")