def lectura_de_archivo(nombre):
    matriz = []
    f = open(nombre)
    for line in f:
        line = line[:-1]
        line = line.split(",")
        matriz.append(line)
    return(matriz)


def crear_transpuesta(matriz):
    
    transpuesta = []
    for j in range (len(matriz[0])):
        lista = []
        for i in range (len(matriz)):
            lista.append(matriz[i][j])
        transpuesta.append(lista)
    return(transpuesta)


def main():
    pass
    mat = lectura_de_archivo("/workspaces/AD23TC1028-411/8-Matrices/datos.txt")
    trans = crear_transpuesta(mat)
    print(trans)
if __name__ == "__main__":
    main()