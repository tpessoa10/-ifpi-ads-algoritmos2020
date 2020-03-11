def main(): 
    n = int(input('Digite um valor: '))
    do_twice(print_twice, n)
    do_four()

def do_twice(f, n=2):
    f()
    f()
    print(n)
    print(n)


def print_spam():
    print('spam')


def print_twice():
    print('spam')
    print('spam')


def do_four():
    def do_twice(f, n=2):   
        f()
        f()   
    def do_twice(f, n=2):
        f()
        f()


main()
