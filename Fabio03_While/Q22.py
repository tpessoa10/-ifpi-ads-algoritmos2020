def main():


    n = int(input('Quantas fichas deseja ler: '))
    c = 1

    mais_magro = 0
    mais_gordo = 0
    num_gordo = 0
    num_magro = 0


    while c <= n:
        num_indent = int(input('Digite o número de indentificação: '))
        nome = input('Digite o nome: ')
        peso = float(input('Digite o peso: '))
        
        if peso < mais_magro:
            mais_magro = peso
            num_magro = num_indent
            nome_magro = nome

        if peso > mais_gordo:
            mais_gordo = peso
            mais_magro = mais_gordo
            num_gordo = num_indent
            nome_gordo = nome

        c = c + 1


    print('O boi mais gordo pesa {} e o número de indentificacao é {}'.format(mais_gordo, num_gordo))
    print('O boi mais magro pesa {} e o número de indentificacao é {}'.format(mais_magro, num_magro))


main()

