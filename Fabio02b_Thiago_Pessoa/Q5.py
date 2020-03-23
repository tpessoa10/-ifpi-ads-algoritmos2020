def main():
    produto1 = float(input('Digite o preço do primeiro produto: '))
    produto2 = float(input('Digite o proço do segundo produto: '))
    produto3 = float(input('Digite o preço do terceiro produto: '))

    produto_barato(produto1,produto2,produto3)


def produto_barato(produto1, produto2, produto3):
    if produto1 < produto2 and produto1 < produto3:
        print('O primeiro produto é o mais barato ')
    elif produto2 < produto1 and produto2 < produto3:
        print('O segundo produto é o mais barato ')
    elif produto3 < produto1 and produto3 < produto2:
        print('O terceiro produto é o mais barato ')


main()

