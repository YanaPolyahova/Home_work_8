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
