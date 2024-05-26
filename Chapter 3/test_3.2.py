import requests
with open('/Users/pluser/PycharmProjects/Python_Ed_1/Chapter 3/dataset_3378_3.txt', 'r+') as file:
    s = file.readline().strip()
    r = requests.get(s)
    while True:
        if not r.text.startswith('We'):
            r = requests.get('https://stepik.org/media/attachments/course67/3.6.3/' + r.text)
        else:
            print(r.text)
            break

