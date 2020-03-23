def main():
    n = int(input('Digite um número de quatro digitos: '))

    milhar = n // 100
    dezena = n % 100

    quadrado_perfeito(milhar, dezena, n)

    print(f'A soma de {milhar} + {dezena} = {milhar + dezena} e a raiz quadrada é {n**(1/2)}')

def quadrado_perfeito(milhar, dezena, n):
    if milhar + dezena == n**(1/2):
        print('Quadrado perfeito')
    else:
        print('Não é um quadrado perfeito')

    
main()

