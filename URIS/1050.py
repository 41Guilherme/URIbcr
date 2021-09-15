lista = [[11,"São Paulo"],
         [61,"Brasilia"],
         [71,"Salvador"],
         [21,"Rio de Janeiro"],
         [32,"Juiz de Fora"],
         [19,"Campinas"],
         [27,"Vitoria"],
         [31,"Belo Horizonte"]]

x = int(input())
i = 0
verefica = True
while (i < 8):
    if lista[i][0] == x:
        print(lista[i][1])
        verefica = True
        break
    else:
        i = i + 1
        verefica = False

if not verefica:
    print("DDD não cadastrado")




