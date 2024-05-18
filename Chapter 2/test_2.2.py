'''n = int(input())
a = []
for i in range(1, n+1):
    if len(a) >= n:
        break
    for j in range(1, i+1):
        a.append(i)
        if len(a) >= n:
            break
print(*a)'''

n = int(input())
a = []
for i in range(1, n+1):
    if len(a) >= n:
        break
    a += [i] * i
print(*a[:n])

