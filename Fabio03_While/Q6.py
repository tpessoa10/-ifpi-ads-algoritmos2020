def main():

    n = int(input("Tabuada de:"))
    x = 1
    while x <= 10:
        a = n * x
        print('{} x {} = {}'.format(n, x, a))
        x = x + 1

main()

