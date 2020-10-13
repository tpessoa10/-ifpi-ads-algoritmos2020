def main():

    print('===== WordPplay =====\n' \
    + '1 - Palavras com + de 20 letras\n' \
    + '2 - Palavras sem "e"\n' \
      '3 - Letra proibida\n'
      '4 - Letras da lista\n'
      '5 - Letras obrigatórias\n'
      '6 - Letras em ordem alfabética'  
    + '0 - Sair\n')

    opcao = int(input('Digite sua opcão: '))
    while opcao != 0:
        if opcao == 1:
            mais_20_letras()
        elif opcao == 2:
            has_no_e()
        elif opcao == 3:
            avoids()
        elif opcao == 4:
            uses_only()
        elif opcao == 5:
            user_all()
        elif opcao == 6:
            is_abecedarian()
    
def mais_20_letras():
    print('PALAVRAS COM MAIS DE 20 LETRAS')
    arq = open('words.txt')
    for palavra in arq:
        if len(palavra) > 20:
            print(palavra)


def has_no_e():
    print('PALAVRAS SEM A LETRA E')
    arq = open('words.txt')
    sem_e = 0
    tot = 0
    for palavra in arq:
        tot = tot + 1
        if 'e' not in palavra:
            sem_e = sem_e + 1
            print(palavra)
    porcent = (sem_e / tot) * 100
    print('A porcentagem de números sem a letra E é de {}'.format(porcent)) 


def avoids():
    print('LETRAS PROIBIDAS')
    arq = open('words.txt')
    letra_proibida = input('Digite a letra proibida: ')
    sem_letra = 0
    for palavra in arq:
        if letra_proibida not in palavra:
            sem_letra = sem_letra + 1
    print('A quantidade de palavras sem as letras proibidas é {}'.format(sem_letra))


def uses_only():
    palavra = input('Digite uma palavra: ')
    letras = input('Digite as letras(Colocar espaco entre cada letra): ').split(' ')
    for letra in palavra:
        if letra not in letras:
            return False
    print('É formado pelas letras')

    
def user_all():
    palavra = input('Digite uma palavra: ')
    letras_obrigatorias = input('Digite as letras obrigatorias(Colocar espaco entre as letras): ').split(' ')
    for letra in palavra:
        if letra not in letras_obrigatorias:
            return False
    print('Usa todas as letras obrigatórias')

def is_abecedarian():
    palavra = input('Digite uma palavra: ')
    anterior = palavra[0]
    for letra in palavra:
        if letra < anterior:
            return False
        anterior = letra
    print('As palavras estão em ordem alfábetica')
    ant = 0
    for i in range(0, len(palavra)):
        if i > ant:
            ant = ant + 1
    print(f'Existem {ant} letras em ordem alfabetica')


main()

