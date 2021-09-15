t = int(input())
n1 = []
n2 = 0

if (t >= 2 and t <= 50):
    for j in range(1000):
        for i in range(t):
            n1.append(i)

    for l in n1:
        print("N[{}] = {}".format(n2,l))
        n2 = n2 + 1
        if n2 == 1000:
            break


    
