with open('/Users/pluser/PycharmProjects/Python_Ed_1/Chapter 3/dataset_3380_5.txt', 'r+') as file:
    a = []
    d = {}
    for line in file:
        a.append(line.strip('\n').split('\t'))
    for c in a:
        if int(c[0]) in d:
            d[int(c[0])].append(int(c[2]))
        else:
            d[int(c[0])] = [int(c[2])]

    for k in sorted(d.keys()):
        print(k, '', sum(d[k]) / (len(d[k])))




