lista = [10,2,5,7,6,3]
n=len(lista)
soma = 0
for i in range (n):
    if(lista[i]%2==0):
        soma += lista[i]
        print(f'O somatorio dos elementos pares da lista é:{soma}')