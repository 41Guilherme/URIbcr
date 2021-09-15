x = True
while x:
    try:
        valor = int(input())
        i = 0
        while(valor > 1):
            n = n // 2
            i = i + 1
        print(i)

    except EOFError:
        break