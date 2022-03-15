'''
decorators são funções
envolvem outras funções e aprimoram seu comportamento

decorators usam @ (sintactic sugar)
açucar sintático é usado para deixar a funçã mais legível e se for removido não faz diferença no programa

não confunda decorator com decoration functio
o sintactic sugar @decoration_function é um decorator
'''


# # a decorator está "decorando" a função que está sendo passada como parâmetro
# def seja_educado(funcao): # decorator sempre recebe como parâmetro a função que vai decorar
#     def sendo():
#         print('Bom dia')
#         funcao()
#         print('Tenha um bom dia')
#     return sendo


# @seja_educado
# def apresentando():
#     print('I am Cornolio')


# # com o sintactic sugar, chamamos a função de dentro e ele faz o decorator
# # o @seja_educado "emoldurou" apresentando() com seja_educado()
# apresentando()
