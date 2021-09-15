lista = []
nValores = 0
for i in range(5):
    x = int(input())
    lista.append(x)

for i in lista:
    if i % 2 ==0:
        nValores = nValores + 1
        
print("{} valores pares".format(nValores))