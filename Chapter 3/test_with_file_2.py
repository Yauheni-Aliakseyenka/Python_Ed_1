with open('/Users/pluser/PycharmProjects/Python_Ed_1/Chapter 3/dataset_3363_3.txt', 'r+') as file:
    k_max = 0
    line_max = ''
    for line in file:
        line = line.split()
        a = list(line)
        for i in set(a):
            k = a.count(i)
            if k >= k_max:
                k_max = k
                line_max = i
    print(line_max + ' ' + str(k_max))



'''sentence = input().lower().split()
a = list(sentence)
for i in set(a):
    k = a.count(i)
    print(i + ' ' + str(k))'''