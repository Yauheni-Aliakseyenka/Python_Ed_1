with open('/Users/pluser/PycharmProjects/Python_Ed_1/Chapter 3/dataset_3363_2.txt', 'r+') as file:
    s = file.readline().strip()
# s = input()
i = 0
symbol = ''
while i < len(s):
    num = ''
    if s[i].isalpha():
        symbol = s[i]
        i += 1
    while s[i].isdigit():
        num += s[i]
        i += 1
        if i == len(s):
            break
    print(symbol * int(num), end='')









