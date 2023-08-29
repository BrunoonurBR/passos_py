# script funcao1.py
valor = 20

def multiplica(fator):
    global valor
    valor = valor * fator
    print("Resultado", valor)

def main():
    numero =int(input())
    multiplica(numero)
    multiplica(numero)
 
# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual à "__main__".
# Nesse caso, a condição do IF a seguir será TRUE,
# então o que está no corpo do IF será executado. 
# No caso, é um chamado ao método main do script
 
if __name__ == "__main__":
    main()
