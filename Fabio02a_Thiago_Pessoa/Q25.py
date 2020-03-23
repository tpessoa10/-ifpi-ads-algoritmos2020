def main():
    senha = int(input('Digite sua senha: '))

    senha_correta(senha)

def senha_correta(senha):
    if senha == 1234:
        print('Login efetuado com sucesso')
    else:
        print('Senha incorreta tente novamente')
    

main()

