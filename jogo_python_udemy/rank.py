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

"""
from csv import DictReader
from csv import DictWriter

def atualizar_rank(pontuacao, nome):
    lista = []

    # with open('rank.csv', 'a', encoding='utf_8', newline='') as arquivo:
    #     escritor_csv = DictWriter(arquivo, fieldnames=['Pontuação', 'Nome'])
    #     escritor_csv.writerow(pontuacao, nome)

    with open('rank.csv', encoding='utf_8') as arquivo:
        rank = list(DictReader(arquivo, delimiter=','))

    for i in rank:
        lista.append(int(i['Pontuação']))
        
    lista.sort()

    rank_ordenado = []
    for i in range(len(lista)):
        for i in range(len(rank)):
            if int(rank[i]['Pontuação']) == lista[i]:
                rank_ordenado.append(rank[i])

    with open('rank_ordenado.csv', 'w', encoding='utf_8', newline='') as arquivo:
        escritor_csv = DictWriter(arquivo, fieldnames=['Pontuação', 'Nome'])
        escritor_csv.writeheader()
        for i in range(len(rank_ordenado) - 1, -1, -1):
            escritor_csv.writerow(rank_ordenado[i])

    print(pontuacao, nome)

atualizar_rank('asd', 100)

""" 
"""
Pontuação,Nome
5,e
2,b
4,d
1,a
3,c
"""
