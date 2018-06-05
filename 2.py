word = "zapato"
letter_uniques_list = []
letter_list2 = []

for l in word:
  if not l in letter_uniques_list:
    letter_uniques_list.append(l)

for lu in letter_uniques_list:
  n=0
  for l2 in word:
    if lu==l2:
      n=n+1
      letter_list2.append([n, lu])

print('Letter:', sorted(letter_list2)[-1][1])
print('Quantity:', sorted(letter_list2)[-1][0])
    
