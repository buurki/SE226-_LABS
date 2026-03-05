TASK1: Without
Count

x = int(input("enter positive value: "))
if x < 1:
    print("enter positive value")
else:
    while x > 0:
        print(x)

        if x % 2 == 0:
            x = x / 2
        else:
            if x != 1:
                x = 3 * x + 1
            else:
                break

TASK2:






