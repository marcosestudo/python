'''
toda entrada do usuário de ve ser tratada
try / except são bem comuns, else e finally, nem tanto
'''

# try:
#     num = int(input('insir um número\n'))
# except ValueError:
#     print('insira um número, seu animal')
# else:
#     print(f'digitou: {num}') # cai aqui se não der erro no try
# finally:
#     print('finally') # se der erro, executa o except, depois o finally, sem erro executa o else, depois o finally
#                      # sempre cai aqui
#                      # o finally geramente é usado para fechar ou desalocar recursos
#                      # trabalhando com banco de dados, por ex., abrimos a conexao com o BD e devemos fechá-la quando terminamos
#                      # o finally é util pra isso, pra fechar um arquivo que foi aberto para leitura / escrita, etc


def divide(a, b):
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err: # podemos passar uma tupla com város erros
        return f'ocorreu um erro {err}'
