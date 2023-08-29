# script threads_inc.py
from threading import Thread, Lock
from multiprocessing import Process
import time

contador = 0
 
def funcao_a(indice):
    global contador
    for i in range(1000000):
        contador += 1
    print("Termino thread ", indice)

def main():
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()
 
    print("Antes de aguardar o termino!", contador)

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", contador)

if __name__ == "__main__":
    main()
