from os import strerror
try:
    ficheiro = input("Informe o nome do ficheiro: ")
    arquivo = open("C:\\Users\\Euzebio Junior\\Documents\\Diario\\" + ficheiro + ".txt", "rt", encoding="utf-8")
    lista = []
    lista2 = []
    nota = ""
    confirmar = False
    cont = 0
    for x in arquivo.readlines():
        lista.append(x.split())

    conta = (sorted(lista, key=lambda x: x[0]))
    for x in conta:
        for y in lista2:
            if x[0] == y[0]:
                confirmar = True
                y[2] = str(float(y[2]) + float(x[2]))
        if confirmar == False:
            lista2.append(x)

        confirmar = False

    novoarquivo = open("C:\\Users\\Euzebio Junior\\Documents\\Diario\\" + ficheiro + ".hist" + ".txt", "wt",
                       encoding="utf-8")
    for x in lista2:
        for y in x:
            if y.isalpha() == False:
                novoarquivo.write("......"+y)
            else:
                novoarquivo.write(y + " ")
        novoarquivo.write("\n")

    arquivo.close()
    novoarquivo.close()


except IOError as e:
    print("O erro ocorrido foi:",strerror(e.errno))
