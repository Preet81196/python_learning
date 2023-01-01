def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

if __name__ == '__main__':
    print(xo('xo'))
    print(xo('xxOo'))
    print(xo('xxxm'))
    print(xo('Oo'))
    print(xo('ooom'))
