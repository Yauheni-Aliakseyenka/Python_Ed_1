fig_type = input()

if fig_type == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S1 = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S1)

elif fig_type == "прямоугольник":
    a = int(input())
    b = int(input())
    S2 = a * b
    print(S2)

elif fig_type == "круг":
    r = int(input())
    S3 = 3.14 * r**2
    print(S3)

else:
    print("Неверная фигура!")
