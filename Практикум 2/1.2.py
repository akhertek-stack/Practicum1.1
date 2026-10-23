print("Какие два слова передал первой радиограммой Александр Попов?")
word_1 = input()
word_2 = input()
if  word_1 == "генрих"  and word_2 == "герц":
    print("Верно")
elif word_1 == "герц" and word_2 == "генрих":
    print("Верно")
else:
    print("Неверно")