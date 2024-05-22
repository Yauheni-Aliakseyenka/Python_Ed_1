table = []
while True:
    elem_row = input()
    if elem_row == 'end':
        break
    row = [int(x) for x in elem_row.split()]
    table.append(row)

for i in range(len(table)):
    for j in range(len(table[i])):
        new_elem = table[i-1][j] + table[i+1-len(table)][j] + table[i][j-1] + table[i][j+1-len(table[i])]
        print(new_elem, end=' ')
    print()
