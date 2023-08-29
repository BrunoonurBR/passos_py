veiculos = ['aviao', 'carro', 'navio', 'ônibus']

f_maiuscula = lambda x: str.upper(x)

nomes_maiusculos = list(map(f_maiuscula, veiculos))

print(f'nomes maiusculos = {nomes_maiusculos}')

#funcao lambda junto com a funcao pyhton(declarei a funcao de letras em maiusculas na variavel f_mauisculos, apos isso chamei na variavel nomes_maiusculos)
