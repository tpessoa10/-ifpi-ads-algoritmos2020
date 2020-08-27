def main():

    n = int(input('Quantidade de pessoas que irão votar: '))
    c = 1
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    voto_nulo = 0
    voto_branco = 0

    print('-'* 50)
    print('Digite 1, 2, ou 3 para votar em seu candidato')
    print('Digite 9 para votar nulo e 0 para votar em branco')
    print('-'* 50)

    while c <= n:
        voto = int(input('Seu voto: '))
        if voto == 1:
            candidato1 = candidato1 + 1
        elif voto == 2:
            candidato2 = candidato2 + 1
        elif voto == 3:
            candidato3 = candidato3 + 1
        elif voto == 9:
            voto_nulo = voto_nulo + 1
        elif voto == 0:
            voto_branco = voto_branco + 1
        c = c + 1

    if candidato1 > candidato2 > candidato3:
        print('O vencendor da eleição foi o primeiro candidato')
    elif candidato1 > candidato3 > candidato2:
        print('O vencendor da eleição foi o primeiro candidato')
    elif candidato2 > candidato3 > candidato1:
        print('O vencendor da eleição foi o segundo candidato')
    elif candidato2 > candidato1 > candidato3:
        print('O vencendor da eleição foi o segundo candidato')
    elif candidato3 > candidato1 > candidato2:
        print('O vencedor da eleição foi o terceiro candidato')
    elif candidato3 > candidato2 > candidato1:
        print('O vencedor da eleição foi o terceira candidato')


    print('A quantidade de votos no primeiro candidato foi {}'.format(candidato1))
    print('A quantidade de votos no segundo candidato foi {}'.format(candidato2))
    print('A quantidade de votos no terceiro candidato foi {}'.format(candidato3))
    print('A quantidade de votos nulos foi {}'.format(voto_nulo))
    print('A quantidade de votos em branco foi {}'.format(voto_branco))




main()

