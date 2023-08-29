# script processos.py
from threading import Thread
from multiprocessing import Process

minha_lista = []

def adiciona():
    for i in range(100):
        minha_lista.append(1)

def main():
    tarefas = []
 
    for indice in range(10):
        t = Thread(target=adiciona)
        tarefas.append(t)
        t.start()

    for indice in range(10):
        p = Process(target=adiciona)
        tarefas.append(t)
        p.start()

    for tarefa in tarefas:
        tarefa.join()

    print(len(minha_lista))

if __name__ == '__main__':
    main()
