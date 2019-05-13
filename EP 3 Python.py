linha1 = str(input("insira a primeira linha(separado por virgula): "))
linha2 = str(input("insira a segunda linha(separado por virgula): "))
linha3 = str(input("insira a terceira linha(separado por virgula): "))
linha4 = str(input("insira a quarta linha(separado por virgula) Ou 0 para deixar vazio: "))
if linha4 != "0":
    matriz = []
    matriz.append(linha1.split(","))    
    matriz.append(linha2.split(","))
    matriz.append(linha3.split(","))
    matriz.append(linha4.split(","))
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    linhas = []
    k = 1
    for j in matriz[0]:
        lista1.append(int(j))

    for j in matriz[1]:
        lista2.append(int(j))

    for j in matriz[2]:
        lista3.append(int(j))
    for j in matriz[3]:
        lista4.append(int(j))
    linhas = [lista1, lista2, lista3, lista4]
    for j in range(3):
        for i in range(len(lista1)):
            if linhas[j][i] != 1:
                if i != 1 and j != 1:
                    if linhas[j - 1][i] == 1 or linhas[j][i - 1] == 1:
                        linhas[j][i] = k
                    else:
                        k = k +1
            else:
                linhas[j][i] = k


    for j in range(len(linhas)):
        print(linhas[j])

else:
    matriz = []
    matriz.append(linha1.split(","))    
    matriz.append(linha2.split(","))
    matriz.append(linha3.split(","))
    lista1 = []
    lista2 = []
    lista3 = []
    linhas = []
    k = 1
    for j in matriz[0]:
        lista1.append(int(j))

    for j in matriz[1]:
        lista2.append(int(j))

    for j in matriz[2]:
        lista3.append(int(j))
    linhas = [lista1, lista2, lista3]
    for j in range(3):
        for i in range(len(lista1)):
            if linhas[j][i] != 1:
                if i != 1 and j != 1:
                    if linhas[j - 1][i] == 1 and linhas[j][i - 1] == 1:
                        linhas[j][i] = k
                    else:
                        k = k +1


    for j in range(len(linhas)):
        print(linhas[j])
            




















