def eh_primo(n):
    if (n < 2):
        return False
    i=n//2
    while (i > 1):
        if (n % i == 0):
            return False
        i=i-1
    return True

def imprimir_resultado(numero, resultado):
    mensagem= f'O numero{numero} Não é primo'
    if (resultado):
        mensagem= f'O numero {numero} é primo'
    return mensagem
    
numero = 7
resultado = eh_primo(numero)
msg= imprimir_resultado(numero, resultado)
print(msg)