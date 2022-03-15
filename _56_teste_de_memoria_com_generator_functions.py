'''teste de memória '''

# def fib_lista(max):
#     nums = []
#     a, b = 0, 1
#     while len(nums) < max:
#         nums.append(b)
#         a, b = b, a + b
#     return nums

# for n in fib_lista(100000):
#     print(n)


# def fib_gen(max):
#     a, b, contador = 0, 1, 0
#     while contador < max:
#         yield(b)
#         a, b = b, a + b
#         contador += 1

# for n in fib_gen(100000):
#     print(n)





### exercícicos ###


# fib = [1, 1]

# for i in range(5):
#     fib.append(fib[-1] + fib[-2])

# print(fib)


# def fib(max):
#     fib = [1 , 1]
#     while fib[-1] <= max:
#         fib.append(fib[-1] + fib[-2])

#     return(fib)


# # exercício - função generator
# def fib_gen(max):
#     a, b, contador = 1, 1, 0
#     yield 1
#     yield 1
#     while contador <= max:
#         a = b
#         b = a + b
#         yield b
#         contador += 1

# # usando lista com generator expression
# def fib_gen2(max):
#     fib = [1 , 1]
#     while len(fib) <= max:
#         fib.append(fib[-1] + fib[-2])

#     return (num for num in fib)

# teste = fib_gen(100000)

# for i in teste:
#     print(i)
