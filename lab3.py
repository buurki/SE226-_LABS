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


TASK3:
n = int(input("Enter a number between 3 and 9: "))

if n < 3 or n > 9:
    print("Invalid input")
else:
    for k in range(1, 2*n):
        if k <= n:
            print("*" * k)
        else:
            print("*" * (2*n - k))






