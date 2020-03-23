def main():

    for i in range(1000, 10000):
        milhar = i // 100
        dezena = i % 100
        if dezena + milhar == i**(1/2):
            print(f'{i}')




main()

