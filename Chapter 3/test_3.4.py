d = int(input())
s_right = set(input().lower() for i in range(d))

l = int(input())
s_begin = set(input().lower() for j in range(l))
s_new = set()
for row in s_begin:
    for words in set(row.split()):
        s_new.add(words)

errors = []
for k in s_new:
    if k in s_right:
        continue
    else:
        errors.append(k)

print(*errors, sep='\n')



'''e = []
for j in range(l):
    e.append(input().split())
m = set()
for row in e:
    s = set(row)
    for v in s:
        m.add(v)
print(m)'''

