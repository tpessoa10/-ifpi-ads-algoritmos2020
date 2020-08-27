def main():

    n = int(input('Quantos termos quer mostrar na sua sequencia: '))
    c = 0
    t1 = 0
    t2 = 1

    print(t1)
    print(t2)

    while c <= n:
        t3 = t1 + t2
        print(t3)
        t1 = t2
        t2 = t3
        c = c + 1


main()

