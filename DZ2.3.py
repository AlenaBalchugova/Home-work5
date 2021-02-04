list= ['Зима', "Весна", "Лето", "Лето"]

month = int(input("Введите номер месяца  "))
if month ==1 or month == 2 or month == 12:
        print(list[0])
elif month == 3 or month == 4 or month ==5:
    print(list[1])
elif month == 6 or month == 7 or month == 8:
    print(list[2])

elif month == 9 or month == 10 or month == 11:
    print(list[3])
else:
        print("Такого месяца не нет введите номер с 1 до 12")