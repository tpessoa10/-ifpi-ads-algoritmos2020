def main():


    n = int(input('Digite um número: '))
    c = 0
    r = 0

    while c <= n:
        c= c + 1
        raiz = c**(1/2)
        if raiz == int(raiz):
            r = raiz


    num = r * r

    print('O maior quadrado menor que {} é {} (quadrado de {})'.format(n, num, r))


main()

