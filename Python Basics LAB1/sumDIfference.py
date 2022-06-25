num1 = int(input("Enter a number \t"))
num2 = int(input("Enter another number \t"))

def addDifference():
    sum = num1 + num2
    print("Sum:\t", sum)
    differnece = abs(num1 - num2)
    print("Difference:\t", differnece )
    Prodct = num1 * num2
    print("Product :", Prodct)
    quotnt =  int(num1 / num2)
    print("Quotient :", quotnt, "\n")

addDifference()