#Tesk_1

month = input("Введите месяц вашего рождения:").lower()
data = input("Введите дату вашего рождения:")
if (month == "март" and "21" <= data <= "31") or (month == "апрель" and "1" <= data <= "19"):
    print("Овен")
elif (month == "апрель" and "30" >= data >= "21") or (month == "май" and "1" <= data <= "20"):
    print("Телец")
elif (month == "май" and "31" >= data >= "21") or (month == "июнь" and "1" <= data <= "20"):
    print("Близнецы")
elif (month == "июнь" and "30" >= data >= "21") or (month == "июль" and "1" <= data <= "22"):
    print("Рак")
elif (month == "июль" and "31" >= data >= "23") or (month == "август" and "1" <= data <= "22"):
    print("Лев")
elif (month == "август" and "31" >= data >= "23") or (month == "сентябрь" and "1" <= data <= "22"):
    print("Дева")
elif (month == "сентябрь" and "30" >= data >= "23") or (month == "октябрь" and "1" <= data <= "22"):
    print("Весы")
elif (month == "октябрь" and "31" >= data >= "23") or (month == "ноябрь" and "1" <= data <= "21"):
    print("Скорпион")
elif (month == "ноябрь" and "30" >= data >= "22") or (month == "декабрь" and "1" <= data <= "21"):
    print("Стрелец")
elif (month == "декабрь" and "31" >= data >= "22") or (month == "январь" and "1" <= data <= "19"):
    print("Козерог")
elif (month == "январь" and "31" >= data >= "20") or (month == "февраль" and "1" <= data <= "18"):
    print("Водолей")
elif (month == "февраль" and "29" >= data >= "19") or (month == "март" and "1" <= data <= "20"):
    print("Рыбы")
else:
    print("Данные введены не корректно. Повторите ввод.")

#Tesk_2
interest_rate = 10
location_program = 2
children_program = 1
salary_program = 0.5
insurance_program = 1.5
yes = "Да"
no = "Нет"
location = input("Введите регион проживания:").capitalize()
children = int(input("Введите количество детей:"))
salary = input("Являетесь ли вы зарплатным клиентом банка (Да/Нет):").capitalize()
insurance = input("Планируете ли оформлять страхование в нашем банке (Да/Нет):").capitalize()
if location == "Амурская Область" or "Еврейская Автономная Область" or "Забайкальский Край" or "Камчатский Край" or "Магаданская Область" or "Приморский край" or "Республика Бурятия" or "Республика Саха" or "Сахалинская Область" or "Хабаровский край" or "Чукотский Автономный Округ":
    print("Ваша процентная ставка составит 2 %")
elif children > 3 and salary == yes and insurance == yes:
    print("Ваша процентная ставка равна", interest_rate - children_program - salary_program - insurance_program)
elif children > 3 and salary == no and insurance == yes:
    print("Ваша процентная ставка равна", interest_rate - children_program - insurance_program)
elif children > 3 and salary == yes and insurance == no:
    print("Ваша процентная ставка равна", interest_rate - children_program - salary_program)
elif children > 3 and salary == no and insurance == no:
    print("Ваша процентная ставка равна", interest_rate - children_program)
elif children <= 3 and salary == yes and insurance == yes:
    print("Ваша процентная ставка равна", interest_rate - salary_program - insurance_program)
elif children <= 3 and salary == no and insurance == yes:
    print("Ваша процентная ставка равна", interest_rate - insurance_program)
elif children <= 3 and salary == yes and insurance == no:
    print("Ваша процентная ставка равна", interest_rate - children_program - salary_program)
elif children <= 3 and salary == no and insurance == no:
    print("Ваша процентная ставка равна", interest_rate)
