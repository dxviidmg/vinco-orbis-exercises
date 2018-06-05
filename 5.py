lista = [88, 34, 13, 88, 1, 2, 81, 15, 77, 13, 50]
lista2 = []

for n in lista:
  if not n in lista2:
    lista2.append(n)

print('Lista original:', lista)
print('Lista sin repetidos:', lista2)
