with open('/Users/pluser/PycharmProjects/Python_Ed_1/Chapter 3/dataset_3363_4.txt', 'r+') as file:
    sr_full = [0, 0, 0]
    count = 0
    for line in file:
        line = line.strip().split(';')
        a = list(line)
        summa = 0
        for i in range(1, len(a)):
            summa += int(a[i])
            sr_full[-i] += int(a[i])
        sr = summa / 3
        #print(round(sr, 9))
        file.write(str(round(sr, 9)) + '\n')
        count += 1
    for j in sr_full[::-1]:
        file.write(str(round(int(j) / count, 9)) + ' ')
        #print(round(int(j) / count, 9), end=' ')
