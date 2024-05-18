summa = 0
summaSq = 0
while True:
    a = int(input())
    summaSq += a ** 2
    summa += a
    if summa == 0:
        break
print(summaSq)