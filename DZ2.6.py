
count = int(input("Введите сколько у нас товара "))
a = 1
opisanie = []
list = []
name = {}
while a <= count:
    opisanie = dict({'название': input("введите название "),
                    'цена': input("Введите цену "),
                    'количество': input('Введите количество '),
                    'eд': input("Введите единицу измерения ")})
    list.append((a, opisanie))
    a+= 1
    name = dict(
        {'название': opisanie.get('название'),
         'цена': opisanie.get('цена'),
         'количество': opisanie.get('количество'),
         'ед': opisanie.get('ед')})
print(list)
print(name)
