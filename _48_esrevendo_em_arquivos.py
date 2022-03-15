'''
abrindo o arqivo para escrita no modo 'w', ele será sobrescrito
no modo append 'a', o novo texto será adicionado no fimdo arquivo

somente o arquivo é parâmetro obrigatório
parâmetros opcionais

open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

'r' open for reading (default)
'w' open for writing, truncating the file first
'x' open for exclusive creation, failing if the file already exists
'a' open for writing, appending to the end of file if it exists
'b' binary mode
't' text mode (default)
'+' open for updating (reading and writing)
'''


# with open('arquivo.txt', 'w') as arquivo:
#     arquivo.write('1 primeira linha escrita.\n') # o arqivo em modo de escrita 'w' será sobrescrito
#     arquivo.write('2 segunda linha escrita.')


with open('novo.txt', 'w') as arquivo: # se o arquivo não existir, será criado
    arquivo.write('1 primeira linha escrita.\n')
    arquivo.write('2 segunda linha escrita.\n')


# append
with open('novo.txt', 'a') as arquivo: # se o arquivo não existir, será criado
    arquivo.write('3 primeira linha escrita com append.\n')
    arquivo.write('4 segunda linha escrita com append.\n')


'''
para escrever no início do arquivo existente
crie um novo arquivo; escreva a linha nova nele; copie o texto do antigo e dê um append novo
'''
