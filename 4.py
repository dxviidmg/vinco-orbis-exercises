matriz = [[1, 5, 8, 6], [4, 8, -5, 4]]
transpuesta = [[0, 0], [0, 0], [0, 0], [0, 0]]

for x in range(0, len(matriz)):
  for y in range(0, len(matriz[0])):
    transpuesta[y][x] = matriz[x][y]

print('Matriz original:', matriz)
print('Matriz transpuesta', transpuesta)
