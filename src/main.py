def es_primo(numero: int) -> bool:
    if numero < 2:
        return False

    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


try:
    numero = int(input("Ingresa un número entero: "))
except ValueError:
    print("Entrada no válida: debes ingresar un número entero.")
else:
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")