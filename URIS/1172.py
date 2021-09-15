lista= []
k = 0

for i in range(10):
    x = int(input())
    if x > 0:
        lista.append(x)
    else:
        lista.append(1)

for j in lista:
    print("X[{}] = {}".format(k,j))
    k = k + 1