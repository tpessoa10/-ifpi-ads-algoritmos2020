def main():
    menu = '*** Operações com listas ***'
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar valor na posição'
    menu += '\n 3 - Mostrar todos os valores'
    menu += '\n 4 - Remover valor na posição'
    menu += '\n 5 - Atualizar valor na posição'
    menu += '\n 6 - Quantidade de números pares'
    menu += '\n 7 - Quantidade de números impares'
    menu += '\n 8 - Quantidade de números positivos'
    menu += '\n 9 - Quantidade de números negativos'
    menu += '\n 10 - Quantidade de números zerados'
    menu += '\n 11 - Média da lista'
    menu += '\n 12 - Dobro dos pares'
    menu += '\n 13 - Dividir impares'
    menu += '\n 14 - Números repetidos'
    menu += '\n 15 - Remover todos'
    menu += '\n 16 - Números primos'
    menu += '\n 0 - Sair '
    menu += '\n\n Opção >>> '

    lista = []

    while True:  
        opcao = int(input(menu))
        if opcao == 1:
            inserir_valores(lista)
        elif opcao == 2:
            mostrar_valor_posicao(lista)
        elif opcao == 3:
            mostrar_todos_valores(lista)
        elif opcao == 4:
            remover_valor(lista)
        elif opcao == 5:
            atualizar_posicao(lista)
        elif opcao == 6:
            par(lista)
        elif opcao == 7:
            impar(lista)
        elif opcao == 8:
            positivos(lista)
        elif opcao == 9:
            negativos(lista)
        elif opcao == 10:
            zerados(lista)
        elif opcao == 11:
            media(lista)
        elif opcao == 12:
            dobrar_pares(lista)
        elif opcao == 13:
            dividir_impares(lista)
        elif opcao == 14:
            numeros_repetidos(lista)
        elif opcao == 15:
            remover_todos(lista)
        elif opcao == 16:
            numeros_primos(lista)
        elif opcao == 0:
            break
        else:
            print('Opção inválida')


def inserir_valores(lista):
    quant_valores = int(input('Digite quantos valores deseja adicionar: '))
    for i in range(quant_valores):
        lista.append(int(input('Valores que deseja adicionar: ')))
    print('Os valores na lista são:{}'.format(lista))



def mostrar_valor_posicao(lista):
    posicao = int(input('Digite a posição do valor que deseja ver: '))
    print('O valor é: {}'.format(lista[posicao]))



def mostrar_todos_valores(lista):
    print('Os valores na lista são:')
    for i in lista:
        print(f'{i}')



def remover_valor(lista):
    remover = int(input('Digite a posição em que deseja remover o valor: '))
    lista.pop(remover)
    print('A lista fica:{}'.format(lista))



def atualizar_posicao(lista):
    posicao = int(input('Digite a posição que deseja atualizar: '))
    valor = int(input('Qual valor deseja adicionar nessa posição: '))
    lista[posicao] = valor
    print('A lista fica:{}'.format(lista))


def par(lista):
    par = 0
    for num in lista:
        if num % 2 == 0:
            par = par + 1
    print('A quantidade de números pares é {}'.format(par))



def impar(lista):
    impar = 0
    for num in lista:
        if num % 2 != 0:
            impar = impar + 1
    print('A quantidade de números impares é {}'.format(impar))



def positivos(lista):
    positivo = 0
    for num in lista:
        if num >= 1:
            positivo = positivo + 1
    print('A quantidade de números positivos é {}'.format(positivo))


def negativos(lista):
    negativo = 0
    for num in lista:
        if num <= -1:
            negativo = negativo + 1
    print('A quantidade de números negativos é de {}'.format(negativo))


def zerado(lista):
    zerados = 0
    for num in lista:
        if num == 0:
            zerados = zerados + 1
    print('A quantidade de números zerados é {}'.format(zerados))



def dobrar_pares(lista):
    for num in lista:
        if num % 2 == 0:
            lista[num] = lista[num] * 2
    print('A lista fica {}'.format(lista))



def dividir_impares(lista):
    for num in lista:
        if num % 2 != 0:
            lista[num] = lista[num] // 2
    print('A lista fica {}'.format(lista))


def remover_todos(lista):
    lista.clear()
    print('A lista fica {}'.format(lista))


def media(lista):
    for num in lista:
        soma += num
    media = soma // len(lista)


def zerados(lista):
    zerado = 0
    for num in lista:
        if num == 0:
            zerado = zerado + 1
    print('A quantidade de números zerados é {}'.format(zerado))
        

def numeros_repetidos(lista):
    ocorrencia = 0
    numero = int(input('Qual número deseja ver: '))
    for num in lista:
        if num == numero:
            ocorrencia = ocorrencia + 1
    print('Esse número se repete {} vezes'.format(ocorrencia))

def numeros_primos(lista):
    primos = []
    for num in lista:
        if eh_primo(num) == True:
            primos.append(num)
    
    print('A quantidade de números primos é de {}'.format(len(primos)))
    

def eh_primo(num):
    cont = 0
    for c in range(1, num+1):
        if num % c == 0:
            cont += 1

    if cont == 2:
        return True
    else: 
        return False

main()


