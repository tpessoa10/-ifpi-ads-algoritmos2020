n = int(input('Quantos intens deseja colocar na sua lista: '))
c = 1
soma = 0
cont = 1

while c <= n:
    lista = int(input('Digite um número: '))
    c = c + 1

while cont <= n:
    soma = soma + lista
    cont = cont + 1

media = soma // n

print('A soma dos números é {}'.format(soma))
print('A media dos números é {}'.format(media))

