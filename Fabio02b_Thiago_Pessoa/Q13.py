def main():
    cont = 0
    a = input('Você telefonou para a vitima?(S/N) ').strip()
    b = input('Você esteve no local do crime?(S/N) ').strip()
    c = input('Você mora perto da vítima?(S//N) ').strip()
    d = input('Você devia para a vítima?(S/N) ').strip()
    e = input('Você ja trabalhou com a vítima?(S/N) ').strip()

    eh_suspeito(a, b, c, d, e, cont)


def eh_suspeito(a, b, c, d, e, cont):
    if a in 'Ss':
        cont = cont + 1

    if b in 'Ss':
        cont = cont + 1

    if c in 'Ss':
        cont = cont + 1

    if d in 'Ss':
        cont = cont + 1

    if e in 'Ss':
        cont = cont + 1

    if cont == 1 or cont == 0:
        print('Inocente')
    elif cont == 2:
        print('Suspeito')
    elif cont == 3 or cont == 4:
        print('Cúmplice')
    elif cont == 5:
        print('Assassino')


main()

