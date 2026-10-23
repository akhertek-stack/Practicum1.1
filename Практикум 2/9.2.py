ans1 = input("Собака короткошерстной породы? ").lower()

if ans1 == "да":
    ans2 = input("Рост собаки менее 50 см? ").lower()
    if ans2 == "да":
        ans3 = input("У собаки короткий хвост? ").lower()
        if ans3 == "да":
            print("английский бульдог")
        else:
            ans4 = input("У собаки длинные уши? ").lower()
            if ans4 == "да":
                print("гончая")
            else:
                ans5 = input("У собаки короткое тело? ").lower()
                if ans5 == "да":
                    print("мопс")
                else:
                    print("чихуахуа")
    else:
        ans3 = input("Собака весит более 50 кг? ").lower()
        if ans3 == "да":
            print("датский дог")
        else:
            print("фоксхаунд")
else:
    ans2 = input("Рост собаки менее 50 см? ").lower()
    if ans2 == "да":
        ans3 = input("У собаки доброжелательный характер? ").lower()
        if ans3 == "да":
            print("кокер-спаниель")
        else:
            print("ирландский сеттер")
    else:
        ans3 = input("У собаки рост менее 70 см? ").lower()

        if ans3 == "да":
            ans4 = input("У собаки длинные уши? ").lower()
            if ans4 == "да":
                print("большой вандейский грифон")
            else:
                print("колли")
        else:
            ans4 = input("Окрас рыжий с белыми отметинами? ").lower()

            if ans4 == "да":
                print("сенбернар")
            else:
                ans5 = input("Белоснежный окрас? ").lower()
                if ans5 == "да":
                    print("ирландский волкодав")
                else:
                    print("ньюфаундленд")