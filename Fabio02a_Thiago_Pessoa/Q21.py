def main():
    n = float(input('Digite um número que deseja arredondar: '))
    
    arredondar_numero(n)
    
def arredondar_numero(n):
    num = n // 1
    decimal = n % 1
    if decimal >= 0.5:
        num_arredondado = n + 1 - decimal
        print(f'O número arredondado é {num_arredondado}')
    elif decimal < 5.0:
        num_arredondado = num 
        print(f'O número arredondado é {num_arredondado}')


main()

