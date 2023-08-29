from functools import reduce

f_soma = lambda x,y: x + y

numeros = [1,2,3,4,5,6,7,8,9,10]

resultado = reduce(f_soma, numeros)

print(resultado)

#foi aplicado a funcao reduce, sempre lembrar que tem que ser instalado a biblioteca
