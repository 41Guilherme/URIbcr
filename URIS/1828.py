n = int(input())

for i in range(n):
    entrada = input().split()
    Sheldon , Raj = entrada

    if Sheldon == Raj:
        x = "De novo!"   
    elif Sheldon == "pedra":
        if Raj == "tesoura" or Raj == "lagarto":
            x = Sheldon
        else:
            x = Raj
    elif Sheldon == "papel":
        if Raj == "pedra" or Raj == "Spock":
            x = Sheldon
        else:
            x = Raj
    elif Sheldon == "tesoura":
        if Raj == "lagarto" or Raj == "papel":
            x = Sheldon
        else:
            x = Raj
    elif Sheldon == "lagarto":
        if Raj == "Spock" or Raj == "papel":
            x = Sheldon
        else:
            x = Raj
    elif Sheldon == "Spock":
        if Raj == "tesoura" or Raj == "pedra":
            x = Sheldon
        else:
            x = Raj

    if x == Sheldon:
        x = "Bazinga!"
    elif x == Raj:
        x = "Raj trapaceou!"


    print("Caso #{}: {}".format(i + 1,x))