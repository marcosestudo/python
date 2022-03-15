'''
o bloco try / except em outras linguagens contuma se chamar try / catch
try / except trata erros evitando que o programa pare
sintaxe 
      try:
          execução problemática
      except:
          o que fazer em caso de problema
'''

# tratando erro de forma genérica
try:
    nao_declarada()
except:
    print('deu problema')
# o ideal é tratar o erro de forma específica
try:
    nao_declarada()
except NameError as err: # podemos nomear o tipo de erro para printá-lo, por padrão no python usa-se "err"
    print(f'a aplicação gerou o seguinte erro: {err}') # essas mensagens de erro geralmente não são passadas para o usuário
                                                       # são guardadas no log do sitema


try:
    nao_declarada()
except TypeError as erra:
    print(f'a aplicação gerou o seguinte erro: TypeError: {erra}')
except NameError as errb:
    print(f'a aplicação gerou o seguinte erro: NameError: {errb}')
except:
    print('erro inesperado')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None # retorna None se não encontrar a chave, sem tratamento, pararia o programa 
    except:
        None
