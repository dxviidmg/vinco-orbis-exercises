arreglo = [ 1, 2, 3, 4, [5, 6, 7], 8, 9]

def imprimir (miarreglo):
    for e in miarreglo:
        if isinstance(e, list):
            imprimir(e)
        else:
            print(e)

imprimir(arreglo)
