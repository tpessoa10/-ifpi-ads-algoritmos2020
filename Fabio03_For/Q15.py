def main():


    n = int(input('Digite quantos termos terá sua sequencia: '))
    c = 2
    t1 = 1
    t2 = 3

    print(t1)
    print(t2)

    for i in range(n):
        c = c + 1
        t3 = t2 + c
        t1 = t2
        t2 = t3
        print(t3)
        
    




main()

