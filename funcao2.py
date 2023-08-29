# script funcao2.py
valor = 20

def multiplica(valor, fator):
    valor = valor * fator
    return valor

def main():
    numero = int(input())
    print("Resultado", multiplica(valor, numero))
    print("Resultado", multiplica(valor, numero))

if __name__ == "__main__":
    main()
