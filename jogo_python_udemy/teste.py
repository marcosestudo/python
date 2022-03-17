from csv import DictReader
from csv import DictWriter

def atualizar_rank(pontuacao: int, nome: str, adicionado: int = 0) -> None:
    lista = []

    with open('rank.csv', 'a', encoding='utf_8', newline='') as arquivo:
        escritor_csv = DictWriter(arquivo, fieldnames=['Pontuação', 'Nome', 'Adicionado'])
        escritor_csv.writerow({'Pontuação' : pontuacao, 'Nome' : nome, 'Adicionado' : adicionado})

    with open('rank.csv', encoding='utf_8') as arquivo:
        rank = list(DictReader(arquivo, delimiter=','))

    for i in rank:
        lista.append(int(i['Pontuação']))
        
    lista.sort()

    rank_ordenado = []
    for i in range(len(lista)):
        for j in range(len(rank)):
            print(rank[j])
            if int(rank[j]['Pontuação']) == lista[i] and not int(rank[j]['Adicionado']):
                rank_ordenado.append(rank[j])
                rank[j]['Adicionado'] = 1

    with open('rank.csv', 'w', encoding='utf_8', newline='') as arquivo:
        escritor_csv = DictWriter(arquivo, fieldnames=['Pontuação', 'Nome', 'Adicionado'])
        escritor_csv.writeheader()
        for i in range(len(rank_ordenado) - 1, -1, -1):
            escritor_csv.writerow(rank_ordenado[i])


atualizar_rank(32, 'teste')

"""
Pontuação,Nome
5,e,False
2,b,False
4,d,False
1,a,False
3,c,False
"""