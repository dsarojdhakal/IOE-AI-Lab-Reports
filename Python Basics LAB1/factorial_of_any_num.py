n = int(input("Enter a number:\t"))

def factorial():
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    print("Factorial:", fact)

factorial()