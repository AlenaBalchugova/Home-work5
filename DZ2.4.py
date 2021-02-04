long_str  = input("введите слова через пробел ")
words = []
num = 1
for l in range(long_str.count(' ') + 1):
    words = long_str.split()
    if len(str(words)) <= 10:
        print(f" {num} {words [l]}")
        num += 1
    else:
        print(f" {num} {words [l] [0:10]}")
        num += 1