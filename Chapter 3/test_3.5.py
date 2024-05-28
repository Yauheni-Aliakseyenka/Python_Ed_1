n = int(input())
i = 0
way = {'север':0, 'юг':0, 'запад':0, 'восток':0,}
while i < n:
    side, j = input().split()
    for keys in way:
        if side == keys:
            way[side] += int(j)
    i += 1
print(way['восток'] - way['запад'], way['север'] - way['юг'])
