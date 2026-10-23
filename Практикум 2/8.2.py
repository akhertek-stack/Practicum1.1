mark = "Марк"
age_mark = 78

user = input("Здравствуйте! Как Вас зовут? ")
print(f"Очень приятно, {user}! Меня зовут {mark}.")

age_user = int(input("Сколько Вам лет? "))
raznisa = age_mark - age_user

if raznisa > 0:
    print(f"Да, {user}, я старше Вас на {raznisa} лет.")
elif raznisa < 0:
    print(f"Да, {user}, Вы старше меня на {-raznisa} лет.")
else:
    print(f"Да, {user}, мы с Вами ровесники!")

otvet = input("Вам нравится программировать? ").lower()
if otvet == "да":
    print("Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.")
else:
    print("Жаль. Я думал, Вы сможете написать интересную программу для меня.")