n = int(input('Digite um número: '))
c = n
fat = 1

while c != 0:
    fat = fat * c
    c = c - 1
    print(fat)