while True:
    try:
        x = int(input("Digite um numero: "))
        break
    except ValueError:
        print("Entre com um numero válido.")    