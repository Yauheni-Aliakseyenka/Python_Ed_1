number = input()
firstHalf = int(number) // 1000
secondHalf = int(number) % 1000
summaFH = firstHalf % 10 + firstHalf // 100 + (firstHalf // 10) % 10
summaSH = secondHalf % 10 + secondHalf // 100 + (secondHalf // 10) % 10
if summaFH == summaSH:
    print("Счастливый")
else:
    print("Обычный")
