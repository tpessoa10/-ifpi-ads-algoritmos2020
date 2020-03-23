def main():
    letra = input('Digite uma letra: ')

    vogal_conscoante(letra)

def vogal_conscoante(letra):
    if letra in 'AEIOUaeiou':
        print('Vogal')
    elif letra in 'QWRTYIPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm':
        print('Consoante')
    else:
        print('Inválido')


main()

