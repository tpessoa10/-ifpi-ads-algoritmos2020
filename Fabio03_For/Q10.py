def main():

    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))

    for i in range(limite_inferior, limite_superior):
        if i % 2 != 0:
            print(i)


main()

