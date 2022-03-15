'''
sitema de arquivos: navegação
para manipular arquivos do sistema operacional precisamos importar o módulo os
'''


import os


print(os.getcwd()) # retorna o current work directory - pasta atual

os.chdir('..') # change directory, '..' um diretório acima

print(os.getcwd()) # retorna o current work directory - pasta atual

print(os.path.isabs('Udemy\\Python')) # diz se o diretório é absoluto ou relativo
                                      # absoluto é o caminho completo vindo desde a raiz
# devemos usar contrabarra dupla '\\' na verificação de diretórios no windows
# contrabarra simples '\' é o caracterer de escape 
print(os.path.isabs('C:\\Users\\Nando\\Desktop\\Udemy\\Python')) 


print(os.name) # diz o nome do sistema - posix (Linux e Mac); nt(Windows)
# # print(os.uname()) # dá mais informação que o .name, não existe no Windows

import sys 
print(sys.platform) # retorna a arquitetura do Windows

print(os.getcwd())
os.chdir(os.path.join(os.getcwd(), 'Python')) # acrescenta o diretório no caminho com o join() pra acessar com o chdir()
print(os.getcwd())


print(os.listdir())
print(len(os.listdir())) # diz quantos arquivos tem no diretório
scanner = os.scandir() # retorna um objeto com mais detalhes do diretório
print(list(scanner))
scanner.close() # o escandir() deve ser fechado depios de usado
