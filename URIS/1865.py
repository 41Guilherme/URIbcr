Pessoas = int(input())

for i in range(Pessoas):
    x = input().split()
    nome, forca = x
    forca = int(forca)

    if nome == 'Thor':
        print('Y')
    else:
        print('N')