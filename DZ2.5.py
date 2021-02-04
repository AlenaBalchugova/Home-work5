rayt = [7, 5, 3, 3, 2]
print(f"Рейтинг равен {rayt}")
add = int(input("Введите в списке [7, 5, 3, 3, 2] или иное"))
while add != rayt:
    for n in range(len(rayt)):
        if rayt[n] == add:
            rayt.insert(n + 1, add)
            break
        elif rayt[0] < add:
            rayt.insert(0, add)
        elif rayt[-1] > add:
            rayt.append(add)
        elif rayt[n] > add and rayt[n + 1] < add:
            rayt.insert(n + 1, add)
    print(f"Сейчас список состоит из - {rayt}")
    break
