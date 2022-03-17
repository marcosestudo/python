# linhas = [2, 1, 5, 3, 4, 8, 6, 9, 10, 7]

linhas_ordenadas = []

with open('rank.txt', 'r', encoding='utf8') as arquivo:
    # lendo a primeir alinha sem atribuí-la para pular o cabeçãlho
    arquivo.readline()
    rank = arquivo.read().split('\n')
    
# print(rank)

ordenar = []

for linha in rank:
    # print(linha.split(',')[0])
    ordenar.append(linha.split(',')[0])

# limpando espaços vazios, se tiver
while '' in ordenar:
    ordenar.remove('')
while '' in rank:
    rank.remove('')

print(ordenar)

ordenar = [int(num) for num in ordenar]
ordenar.sort()
print(ordenar)

print(rank[0])
# print(len(rank))
# for num in rank:
#     linhas_ordenadas.append(int(num))

# linhas_ordenadas.sort()
# print(linhas_ordenadas)

# with open('rank_ordenado.txt', 'w', encoding='utf8') as arquivo:
#     for linha in linhas_ordenadas:
#         arquivo.write(str(linha) + '\n')
