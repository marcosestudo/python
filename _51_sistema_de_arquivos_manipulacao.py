'''
sistema de arquivos: manipulação
'''

import os
import tempfile


print(os.path.exists('arquivo.txt')) # diz se o arquivo ou pasta existe

open('criado.txt', 'w').close() # cria e fecha o arquivo, tambem pode ser feito com 'a' ou 'x'
with open('criado.txt', 'w') as arquivo:
    pass # só cria, atribiu o arquivo à variável e fecha
         # quando abrimos um bloco em python, ele espera que tenha algo dentro
         # sem nada ele vai reclamar da indentação, por isso colocamos o pass, só pra ter algo ali mesmo sem fazer nada

# # criando com o os
# # mknod() não existe no windows, dá erro de permissão no mac, nesses casos devemos usar as formas acima
# # os.mknod('criado_com_os.txt')
# # os.mknod('Udemy\\Python\\criado_com_os.txt')


# os.mkdir('diretorio') # cria diretório, funciona em qualquer sistema
# os.makedirs('diretorio\\diretorio2\\diretorio3', exist_ok=True) # cria pastas e subpastas
                                                                  # o segundo parâmetro faz não dar erro se a pasta ja existir
# os.rename('diretorio\\diretorio2\\diretorio3', 'diretorio3_renomeado') # foi renomeado e colocado na pasta atual
                                                                         # parar renomear e mantê-lo onde está
                                                                         # devemor ir até a pasta dele com o cwd() 
                                                                         # ou dar o caminho completo como no exemplo abaixo
# os.rename('diretorio\\diretorio2\\Novo Documento de Texto.txt', 'diretorio\\diretorio2\\renomeado')

# os.remove('arquivo_deletado.txt') # remove() não manda pra lixeira, apaga direto 
                                    # tem uma biblioteca pra mandar pra lixeira(send2trash)
                                    # no Windows dá erro se tentar apagar um arquivo que está aberto
                                    # só remove arquivos, rmdir() remove diretórios

# os.remdir('diretorio_deletado.txt') # ´so remove diretórios vazios

# for arquivo in os.scandir('pasta_que_queremos_apagar'): # apagando uma árvore de arquivos limpando a pasta que queremos apagar
#     if arquivo.is_file():                               # limpando a pasta que queremos apagar
#         os.remove(arquivo.path)

# os.removedirs('diretorio_vazio\\diretorio_vazio2\\diretorio_vazio3') # remove uma árvore de diretórios vazios


# with tempfile.TemporaryDirectory() as tmp: # criando pasta e arquivo temporários
#     print(f'diretório temporário criado em {tmp}')
#     with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo_temp:
#         arquivo_temp.write('arquivo temporário criado')
#     input('quando digitar algo, sairá do input, encerrará o progama e o arquivo temporário irá sumir')

with tempfile.TemporaryFile() as tmp:
    tmp.write(bytes('escrito no arquivo temprário\n', 'UTF-8')) # transformando a string em bites-like antes de mandar por arquivo
    tmp.seek(0)                                                 # só dá pra escerver dados binários em arquivos temporários
    print(tmp.read())

temp = tempfile.TemporaryFile()
tmp.write(bytes('escrito no arquivo temprário\n', 'UTF-8')) 
tmp.seek(0)                                                 
print(tmp.read())
tmp.close # sem usar o bloco with devemos fechar o arquivo
