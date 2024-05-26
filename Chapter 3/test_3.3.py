n = int(input())
com_list = [input().split(';') for i in range(n)]

games = 0
win = 0
draws = 0
loses = 0
points = 0

results = {}

for i in range(len(com_list)):
    results[com_list[i][0]] = [games, win, draws, loses, points]
    results[com_list[i][2]] = [games, win, draws, loses, points]

for i in range(len(com_list)):
    com_list[i][1] = int(com_list[i][1])
    com_list[i][3] = int(com_list[i][3])
    if com_list[i][1] > com_list[i][3]:
        results[com_list[i][0]][0] += 1
        results[com_list[i][0]][1] += 1
        results[com_list[i][0]][4] += 3
        results[com_list[i][2]][0] += 1
        results[com_list[i][2]][3] += 1
    elif com_list[i][1] < com_list[i][3]:
        results[com_list[i][0]][0] += 1
        results[com_list[i][0]][3] += 1
        results[com_list[i][2]][0] += 1
        results[com_list[i][2]][1] += 1
        results[com_list[i][2]][4] += 3
    else:
        results[com_list[i][0]][0] += 1
        results[com_list[i][0]][2] += 1
        results[com_list[i][0]][4] += 1
        results[com_list[i][2]][0] += 1
        results[com_list[i][2]][2] += 1
        results[com_list[i][2]][4] += 1

for club, stat in results.items():
    str_stat = list(map(str, stat))
    print(club + ':' + ' '.join(str_stat))




'''sr_full = [0, 0, 0]
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
        #print(round(int(j) / count, 9), end=' ')'''