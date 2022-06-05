# Feito por Pedro Augusto Machado Cardoso


# Inicializa as listas de coordenadas x e coordenadas y.

xs = []
ys = []

# Obtem o nome do arquivo

a = input("Qual a path do arquivo de entrada? ")

# O readlines() faz uma lista n com cada linha como elemento

f = open(a, "r")
n = f.readlines()

# Verifica se o arquivo é vazio

if not n:
	print("Erro lendo o arquivo")

# Adiciona nas listas de coordenadas

for i in n:
	minhaLista = i.split()
	xs.append(int(minhaLista[0]))
	xs.append(int(minhaLista[2]))
	ys.append(int(minhaLista[1]))
	ys.append(int(minhaLista[3]))

print(f"({min(xs)}, {max(ys)}), ({max(xs)}, {min(ys)})")

