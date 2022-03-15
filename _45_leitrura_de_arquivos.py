'''
open() abre o arquivo para leitura
a função open() retorna um _io.TextIOWrapper
se o arquivo não existir da erro FileNotFound

read() para ler o arquivo aberto

close() para fechar o arquivo depois de usado
é preciso fechar o arquivo para que elel fique disponível para ser usado por outros programas
'''


arquivo = open('arquivo.txt')

print(arquivo)
print(type(arquivo))

# print(arquivo.read())
# print(arquivo.read()) # o python usa o recurso chamado cursor parar ler o arquivo
#                       # depois de arquivo, o cursor fica no final do arquivo
#                       # por isso o segundo print não printou nada

arquivo = arquivo.read()
# print(arquivo)
# print(type(arquivo)) # o read() retorna um astring 

lista = list(arquivo.split('\n')) # gerou uma lista co os elementos separados pela quebra de linha
print(len(lista)) # diz quantas linhas tem o arquivo

arquivo = open('arquivo.txt')
print(list((arquivo))) # antes de ler o arquivo, a lista é criada separando por linha automaticamente
                       # depois de lido, ele vira uma string e devemos usar o split('\n')

# antes de ler podemos usar a função readlines() ao invés da list()
arquivo = open('arquivo.txt')
print(arquivo.readlines())
arquivo.seek(0)
print(len(arquivo.readlines())) # no len(lista) printou 6, aqui printou 5 porque o readline não conta a linha vazia no final  


arquivo.seek(0)
print(arquivo.read(5)) # lê os primeiros 5 caracteres


print(arquivo.closed) # checa se o arquivo está fechado, sem parênteses depois do closed

arquivo.close()

print(arquivo.closed)


'''
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
