'''
StringIO
para ler ou escrever dados em arquivos, o software precisa de permissão de leitura ou escrita

StringIO é usado parar criar e ler arquivo em memória sem gravar em disco
'''


from io import StringIO


mensagem = 'string teste\n' # pode-se criar ma string escrita ou uma string vazia para preencher depois
arquivo = StringIO(mensagem) # arquivo = StringIO(mensagem) == arqivo = open('arquivo.txt')


print(arquivo)
print(arquivo.read())


arquivo.write('segunda linha')
arquivo.seek(0) # voltando o cursor pro início pra le o arquivo todo de novo
print(arquivo.read())
