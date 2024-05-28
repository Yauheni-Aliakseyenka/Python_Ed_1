import requests
with open('/Users/pluser/PycharmProjects/Python_Ed_1/Chapter 3/dataset_3378_2.txt', 'r+') as file:
    s = file.readline().strip()
    r = requests.get(s)
    print(len(r.text.splitlines()))

