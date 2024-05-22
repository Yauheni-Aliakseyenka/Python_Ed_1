'''s = input()
count = 0
p = s[0]
for i in s:
    if p == i:
        count += 1
    else:
        print(p + str(count), end='')
        count = 1
    p = i
print(p + str(count))'''

s = input()
count = 1
s_new = ''
i = 0
while i+1 < len(s):
    if s[i] == s[i+1]:
        count += 1
    else:
        s_new += s[i] + str(count)
        count = 1
    i += 1
print(s_new + s[i] + str(count))






