'''
seek() movimenta o cursor pelo arquivo
o read() retorna uma string
devemos passar como parâmetro aposição do cursor nessa string
devemos colocar 0 para o cursor voltar pro início do texto

quando o arquivo é aberto no programa é criada uma conexão chamada streaming
quando terminara de usar devemos fechar a conexão / fechar o arquivo usando a função close()
'''


arquivo = open('arquivo.txt')

print(list(arquivo))
print(arquivo.read())


arquivo.seek(0)
print(arquivo.read())


arquivo.seek(5) 
print(arquivo.read())

arquivo.seek(0)
print(arquivo.readline())
print(arquivo.readline())


linha3 = arquivo.readline()
lista_palavras = linha3.split(' ')
print(lista_palavras)


arquivo.seek(0)
print(arquivo.readlines())


print(arquivo.closed) # checa se o arquivo está fechado, sem parênteses depois do closed

arquivo.close()

print(arquivo.closed)
