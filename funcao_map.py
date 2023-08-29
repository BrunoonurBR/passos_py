# script funcao_map.py
lista = [1, 2, 3, 4, 5]

def triplica(item):
    return item * 3

def main():
    nova_lista = map(triplica, lista)
    print(list(nova_lista))

if __name__ == "__main__":
    main()
