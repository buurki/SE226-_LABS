QUESTION 1:
def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

def main():
    n = int(input("Enter a number: "))
    print("Factorial:", factorial(n))

if __name__ == "__main__":
    main()

QUESTION 2:

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

term = lambda x, n: (x ** n) / factorial(n)
result = 0
def exp_x(x, y):
    global result
    result = 0
    for i in range(y):
        result += term(x, i)
    return result
def main():
    x = float(input("Enter x: "))
    y = int(input("Enter number of terms: "))
    print("Solution :", exp_x(x, y))
if __name__ == "__main__":
    main()



