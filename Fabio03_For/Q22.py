def main():

    n = int(input('Digite a quantidade de fichas: '))
    magro = 0
    gordo = 0
    indent_magro = 0
    indent_gordo = 0

    for i in range(n):
        nome = input('Digite o nome: ')
        num_indent = int(input('Digite o número de indentificação: '))
        peso = int(input('Digite o peso: '))
        if peso < magro:
            magro = peso
            indent_magro = num_indent
        if peso > gordo:
            gordo = peso
            indent_gordo = num_indent

        
    print('O número de indentificação do boi mais magro é {} e o seu peso é {}'.format(indent_magro, magro))
    print('O número de indentificação do boi mais gordo é {} e o seu peso é {}'.format(indent_gordo, gordo))




main()

