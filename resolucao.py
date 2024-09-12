# Ler o caminho do arquivo
path = input("Ïnsira o caminho do arquivo de texto desejado: ")
text_matrix = []

# Ler e transformar o arquivo de texto em uma matriz
with open(path,'r') as file:
    for linha in file:
        text_matrix.append(linha.strip().split(" "))

