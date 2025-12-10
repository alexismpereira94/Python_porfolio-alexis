try:
    resultado = 10/0
    print(resultado)
except ZeroDivisionError:
    print("Error: division por cero")
except ValueError:
    print("error: Valor invalido")
    
