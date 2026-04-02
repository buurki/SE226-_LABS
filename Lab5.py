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


