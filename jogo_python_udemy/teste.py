from csv import DictReader
from csv import DictWriter


lista = []
with open('rank.csv', encoding='utf_8') as arquivo:
    leitor_csv = list(DictReader(arquivo, delimiter=','))

for x in leitor_csv:
    lista.append(int(x['Pontuação']))
    
lista.sort()

rank_ordenado = []
for x in range(len(lista)):
    for y in range(len(leitor_csv)):
        # print(f"{leitor_csv[y]['Pontuação'] = } {lista[x] = }")
        if int(leitor_csv[y]['Pontuação']) == lista[x]:
            rank_ordenado.append(leitor_csv[y])

with open('rank_ordenado.csv', 'w', encoding='utf_8', newline='') as arquivo:
    escritor_csv = DictWriter(arquivo, fieldnames=['Pontuação', 'Nome'])
    escritor_csv.writeheader()
    for i in range(len(rank_ordenado) - 1, -1, -1):
        escritor_csv.writerow(rank_ordenado[i])


# with open('rank.csv', 'w', encoding='utf_8') as arquivo:
#     for linha in range(leitor_csv):
#         if 
"""
Pontuação,Nome
5,e
2,b
4,d
1,a
3,c
"""