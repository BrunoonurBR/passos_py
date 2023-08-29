from time import sleep
from threading import Thread
def tarefa(tempo_espera, mensagem):
    print(f'\nIniciando a tarefa{mensagem}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {mensagem}')

thread = Thread(target=tarefa, args=(2, 'Thread em execução'))
thread.start()
print('\nAguardando pela execução da Thread...')
thread.join()
print("A execução foi concluída!")