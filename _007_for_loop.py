nome = "asd fg"
nome = nome.title()
lista = [1, 2, 3, 4, 5]
num_range = range(1, 20) # vai até o último menos 1
qtd = 5

# print(nome)

# for letra in nome:
#     print(letra)

# print(f"última letra: {letra}")


# for numero in lista:
#     print(numero)

# print(f"último número: {numero}")


# for numero in num_range:
#     print(numero)

# print(f"último do range: {numero}")

# for indice, letra in enumerate(nome):
#     print(f"índice: {indice}; letra: {nome[indice]}")

# print("\nnote a diferença")
# for _, letra in enumerate(nome): # nesse caso o índice não é importante e pode ser descartado, pode-se trocar por um _
#     print(letra)

# print("\nnesse, imprime o enumerate todo que gera uma lista com o índica e a letra")
# for letra in enumerate(nome):
#     print(letra)


for i in range(qtd): # (0,qtd) e (qtd) funcionam da mesma forma
    print(i, end="") # end="" pro print não pular linha automaticamente
