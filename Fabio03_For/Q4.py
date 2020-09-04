def main():

    a = int(input('Digite o valor inicial: '))
    limite = int(input('Digite o limite: '))
    razao = int(input('Digite a razão: '))
    c = 0

    for i in range(a, limite, razao):
        c = i * razao
        print(i)



main()

