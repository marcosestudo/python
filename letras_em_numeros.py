def valor_da_string(string):
    '''calcula o valor de uma string somando o valor de cada letra asd'''
    letras = (' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
               1, 2, 3, 4, 5, 6, 7, 8, 9,
               1, 2, 3, 4, 5, 6, 7, 8, 9)
    
    result = 0    

    letra_num = dict(zip(letras, numeros))

    for letra in string.lower():
        result += letra_num[letra]

    return result


print(valor_da_string(''))
input()
