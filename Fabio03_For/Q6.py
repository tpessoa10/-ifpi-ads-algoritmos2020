def main():

    n = int(input('Qual número deseja ver a tabuada: '))

    for i in range(n, 11):
        print('{} x {} = {}'.format(n, i, n*i))


main()

