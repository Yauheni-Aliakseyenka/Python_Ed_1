a, b, c = int(input()), int(input()), int(input())
maxN = a
minN = c

if b >= maxN and b >= c:
    maxN = b
elif c >= maxN:
    maxN = c

if b <= minN and b <= a:
    minN = b
elif a <= minN:
    minN = a

averageN = (a+b+c) - maxN - minN

print(maxN, '\n', minN, '\n', averageN)
