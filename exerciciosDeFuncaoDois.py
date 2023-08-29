#funcao para arredondar os valores da lista

lista_numeros = [9.56783, 7.57568, 3.00914, 6.2321]

lista_precisao = [2, 2, 3, 3]

arredondamento = lambda x,y: round(x,y)
#A funcao lambda pode receber mais que um padrao de comando
resultado = list(map(arredondamento,lista_numeros, lista_precisao))
#funcao MAP para mapear os valores que serao analisado
print(resultado)
