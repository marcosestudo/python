'''
'''


from csv import writer


# sem passar o segundo argmento (encoding='utf_8'), não estava escrevend letras com acento nem "ç"
# sem o terceiro argumento (newline='') estava punado uma linha entre cada leitura, disseram que é por causa do windows
with open('filmes.csv', 'w', encoding='utf_8', newline='') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    # # o método writerow() recebe um lista e a coloca em uma linha do .cvs
    # escritor_csv.writerow(['Titulo', 'Gênero', 'Duração'])
    # escritor_csv.writerow(['Titulo1', 'Gênero1', 'Duração1'])
    # escritor_csv.writerow(['Titulo2', 'Gênero2', 'Duração2'])
    
    # while filme != 'sair':
    #     filme = input('Nome do filme: ')
    #     if filme != 'sair':
    #         genero = input('Gênero: ')
    #         duracao = input('Duração: ')
    #         escritor_csv.writerow([filme, genero, duracao])


from csv import DictWriter


with open('filmes2.csv', 'w', encoding='utf_8', newline='') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    escritor_csv.writerow({'Título': 'Titulo1', 'Gênero': 'Gênero1','Duração': 'Duração1'})
    escritor_csv.writerow({'Título': 'Titulo2', 'Gênero': 'Gênero2','Duração': 'Duração2'})
