# linhas = [2, 1, 5, 3, 4, 8, 6, 9, 10, 7]

linhas_ordenadas = []

with open('rank.txt', 'r', encoding='utf8') as arquivo:
    # lendo a primeir alinha sem atribuí-la para pular o cabeçãlho
    arquivo.readline()
    texto = arquivo.read().split('\n')
    
# print(texto)

ordenar = []

for linha in texto:
    # print(linha.split(',')[0])
    ordenar.append(linha.split(',')[0])

# limpando espaços vazios, se tiver
while '' in ordenar:
    ordenar.remove('')

print(ordenar)

ordenar = [int(num) for num in ordenar]
ordenar.sort()
print(ordenar)

# print(len(texto))
# for num in texto:
#     linhas_ordenadas.append(int(num))

# linhas_ordenadas.sort()
# print(linhas_ordenadas)

# with open('rank_ordenado.txt', 'w', encoding='utf8') as arquivo:
#     for linha in linhas_ordenadas:
#         arquivo.write(str(linha) + '\n')
