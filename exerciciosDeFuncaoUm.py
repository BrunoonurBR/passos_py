lista = [0,1,1,2,3,5,8,13,21,34]

fTesteParidade = lambda x: x%2 == 0
#chamei na funcao lambda um paremetro X, realizei o teste para ana;isar o resto da funcao chamada(se o resto for igual a 0 ele me retorna um valor booleano(verdadeiro ou falso))
print(f'teste de fTesteparidade(5) = {fTesteParidade(5)}')

pares = list(filter(fTesteParidade, lista))
#na funcao filter eu solicitei que ele me envie somente os valores que forem verdadeiros que no caso seria os pares
print(f'lista de numeros pares = {pares}')

#funcao lambda eh a funcao principal para resolver esse tipo de problema