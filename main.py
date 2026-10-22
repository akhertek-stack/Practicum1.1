#1print("Привет", "Python!")

#2print("Привет", "Python!")

#3s, r  = map(int, input().split())
#print(s+r)

#4print(r" (\___/)")
#print(r" (='.'=)")
#print(r"('')_('')")

#5print("Привет, Python!\nHello, Python!\nBonjour Python!\nHej, Python!\nHola, Python!")

#6name = input("Как Вас зовут? ")
#print("Здравствуйте,", name)
#hobby = input("Что Вам нравится? ")
#print("Отлично!", hobby, "- хорошее увлечение.")

#7login = input("Login: ")
#password = input("Password: ")
#new_password = input("New_password: ")
#print(f"User {login} has changed the password to {new_password} ")

#8song1 = input()
#song2 = input()
#song3 = input()
#song4 = input()
#song5 = input()
#print(song5)
#print(song4)
#print(song3)
#print(song2)
#print(song1)

#9number = input("номер рейса: ")
#rus_name = input("название авиакомпании (на русском языке): ")
#eng_name = input("название авиакомпании (на английском языке): ")
#rus_city = input("город прилета (на русском  языке): ")
#eng_city = input("город прилета (на английском языке):  ")
#print(f"Заканчивается посадка на рейс {number} {rus_name} до {rus_city}")
#print(f"This is the final boarding call for {eng_name} flight {number} to {eng_city}")

#10total = int(input())
#silver_count = 96
#gold_count = silver_count // 16
#silver_price = 48
#silver_total = silver_price * silver_count
#gold_price = (total - silver_total) // gold_count
#print(gold_price)

#12x = int(input())
#y = ((((x+2)*3)-6)//3)-4
#print(y)

#13cm = float(input())
#total_inches = cm / 2.54
#total_feet = total_inches / 12
#total_yards = total_feet / 3
#total_miles = total_yards / 1760
#print(f"Ярды: {total_yards:.2f}")
#print(f"Мили: {total_miles:.2f}")
##print(f"Футы: {total_feet:.2f}")
#print(f"Дюймы: {total_inches:.2f}")

#11

#14
#country = input()
#for word in country.split():
#    print(word)

#15
#chel = 1
#wives = 7
#cats = wives * 7 * 7
#kotenok = cats * 7
#print(chel + wives + cats + kotenok)

#16
#prodaz = float(input())
#pribyl = prodaz * 0.19
#print(f"{pribyl:.2f}")

#17
#ves = float(input())
#vysata = float(input())
#a = ves * 0.45359237
#b = vysata * 0.0254
#imt = a / b ** 2
#print(f"{imt:.2f}")

#18
#gektar_m2 = 10000
#sm_m = 0.01
#liters_m3 = 1000
#print (gektar_m2 * sm_m * liters_m3)

#19
#n, m = map(int, input().split())
#kashdomy = m // (n+1)
#print(kashdomy)

#20
#n, k = map(int, input().split())
#print(n%k)

#21
#meters = float(input())
#miles = int(meters // 1609.344)
#print(miles)

#22
#price = input()
#print(price[-3])

#23
#seconds = int(input())
#hours = seconds // 3600
#min = (seconds % 3600) // 60
#sec = seconds % 60
#print(f"{hours}:{min}:{sec}")

#24
#n = int(input())
#print(n % 2)

#25
#x, y, n = map(int, input().split())

#dohod = (x * 100 + y) * n
#rub = dohod // 100
#kop = dohod % 100

#print(f"{rub} руб. {kop} коп.")