lst = [int(i) for i in input().split()]
x = int(input())
position = []
for i in range(len(lst)):
    if lst[i] == x:
        position.append(i)
if len(position) != 0:
    print(*position)
else:
    print('Отсутствует')
