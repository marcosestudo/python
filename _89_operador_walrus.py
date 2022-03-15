"""O operador walrus permite fazer atribuição e retorno na mesma expressão"""


nome1 = 'asd fg'
print(nome1)


print(nome2 := 'qwert')
print(nome2)


cesta1 = []
fruta1 = input('Informe a fruta: ')
while fruta1 != 'sair':
    cesta1.append(fruta1)
    fruta1 = input('Informe a fruta: ')


cesta2 = []
while fruta2 := input('Informe a fruta: ') != 'sair':
    cesta2.append(fruta2)
