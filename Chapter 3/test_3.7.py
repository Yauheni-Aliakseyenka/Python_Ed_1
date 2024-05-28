def desh(line_which, line_inn, line_shh):
    neww_line = ''
    for i in line_which:
        for j in range(len(line_inn)):
            if i == line_inn[j]:
                neww_line += line_shh[j]
    return neww_line

line_in, line_sh, line_1, line_2 = (input() for i in range(4))

print(desh(line_1, line_in, line_sh))
print(desh(line_2, line_sh, line_in))

'''line_in = input()
line_sh = input()
line_1 = input()
line_2 = input()
new_line_1 = ''
new_line_2 = ''
for i in line_1:
    for j in range(len(line_in)):
        if i == line_in[j]:
            new_line_1 += line_sh[j]

for i in line_2:
    for j in range(len(line_sh)):
        if i == line_sh[j]:
            new_line_2 += line_in[j]

print(new_line_1)
print(new_line_2)'''

