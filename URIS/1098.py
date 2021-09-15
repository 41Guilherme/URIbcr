nCasos = int(input())

for i in range(nCasos):
    x = int(input())
    
    if x != 1:
        verificador = True
        for  i in range(2, x):
            if x % i == 0:
                verificador = False
                break
    else:
        verificador = False

    if verificador:
        print('{} eh primo'.format(x))
    else:
        print('{} nao eh primo'.format(x))