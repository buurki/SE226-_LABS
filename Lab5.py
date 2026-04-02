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

QUESTION 3:
result = 0

def quest3(n):
    global result
    if n == 1:
        result += 1
        return
    quest3(n - 1)
    if n % 2 == 0:
        result = result - (1 / n)
    else:
        result = result + (1 / n)

def main():
    global result
    n = int(input("n değerini gir: "))
    result = 0
    quest3(n)
    print("Sonuç:", result)

if __name__ == "__main__":
    main()



