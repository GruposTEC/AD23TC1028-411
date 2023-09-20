f = open("/workspaces/AD23TC1028-411/7-Listas/tarejtas.txt")
tarjetas = []
for linea in f:
    linea = linea[:-1]
    linea = linea.split(",")
    tarjetas.append(linea)
    print(linea)
print(tarjetas)

str2 = "hola amigo como estas"
print(str2.split("?"))