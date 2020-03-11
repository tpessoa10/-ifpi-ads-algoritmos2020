def main():
    s = input('Digite: ')
    rigth_justify(s)

def rigth_justify(s):
    t = 70 - len(s)
    tot = ' ' * t + s
    print(tot)
    print(len(tot))



main()

