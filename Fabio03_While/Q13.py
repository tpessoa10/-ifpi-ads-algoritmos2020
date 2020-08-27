def main():


    maior = 0
    n = int(input('Quantos números terá sua lista: '))
    c = 1

    while c <= n:
        num = int(input('Digite um número: '))
        c = c + 1

    if c == 1:
        maior = num
    else:
        num > maior
        maior = num

    print('O maior número da lista é {}'.format(maior))
    

main()

