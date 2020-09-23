def main():

	num = int(input())

	for i in range(num):
	    texto = input()
	    novo_texto = ''

	    for letra in texto:
		if  ord(letra) >= 65 and ord(letra) <= 90 or ord(letra) >= 97 and ord(letra) <= 122:
		    novo_texto += chr(ord(letra)+3)
		else:
		    novo_texto += letra

	    novo_texto = novo_texto[::-1]
	    meio = int((len(novo_texto)/2))
	    metade1 = novo_texto[0:meio]
	    metade2 = novo_texto[meio:]
	    nova_metade = ''

	    for letra in metade2:
		nova_metade += chr(ord(letra)-1)

	    texto_final = metade1+nova_metade

	    print(texto_final)


main()
