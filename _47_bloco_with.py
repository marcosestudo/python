'''
bloco with

trabalhando com arquivos
#1. abrir
#2. manipular
#3. fechar

o bloco with cria um contexto de trabalho onde os recursos utilizados são fechados após o bloco
'''

# melhor forma de se trabalhar com arquivos em python
with open('arquivo.txt') as arquivo:
    texto = arquivo.readlines()
    print(arquivo.closed)

print(texto)


print(arquivo.closed)
