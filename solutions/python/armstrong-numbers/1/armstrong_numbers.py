def is_armstrong_number(number):
    numero = str(number)
    largo_numero = len(numero)

    resultado = sum(int(i)**largo_numero for i in numero)

    if resultado == number:
        return True
    else:
        return False
