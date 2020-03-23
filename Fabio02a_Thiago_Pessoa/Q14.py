def main():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundp número: '))
    n3 = int(input('Digite o terceiro número: '))
    n4 = int(input('Digite o quarto número: '))
    n5 = int(input('Digite o quinto número: '))

    media = (n1 + n2 + n3 + n4 + n5) / 5
    print(f'A media é {media}') 

    maior_media(media, n1, n2, n3, n4, n5)

def maior_media(media, n1, n2, n3, n4, n5):
    if n1 > media:
        print(f'{n1} maior que {media}')

    if n2 > media:
        print(f'{n2} maior que {media}')

    if n3 > media:
        print(f'{n3} maior que {media}')

    if n4 > media:
        print(f'{n4} maior que {media}')

    if n5 > media:
        print(f'{n5} maior que {media}')


main()

