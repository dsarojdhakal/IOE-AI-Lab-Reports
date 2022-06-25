lst = []
num = int(input('How many numbers?: '))
def addList():
    for n in range(num):
        numbers = int(input('Enter number '))
        lst.append(numbers)
    print("Sum of elements in given list is :", sum(lst))

addList()