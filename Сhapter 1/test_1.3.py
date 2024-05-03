digit_1 = float(input())
digit_2 = float(input())
operation = input()

if operation == "+":
    print(digit_1 + digit_2)
elif operation == "-":
    print(digit_1 - digit_2)
elif operation == "*":
    print(digit_1 * digit_2)
elif operation == "pow":
    print(digit_1 ** digit_2)

if operation == "div":
    print(digit_1 // digit_2)
elif operation == "/":
    print(digit_1 / digit_2)
elif operation == "mod":
    print(digit_1 % digit_2)
elif (operation == "div" or operation == "/" or operation == "mod") and (digit_2 == 0):
    print("Деление на 0!")
