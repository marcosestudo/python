'''
podemos importar funções dos nossos próprios arquivos .py
'''


import _017_funcoes # importa todo o módulo executando todo o arquivo


_017_funcoes.hello_world()
print(_017_funcoes.variavel_teste_do_aquivo_41)


from _017_funcoes import hello_world # importa só a função também executando todo o arquivo

hello_world()
