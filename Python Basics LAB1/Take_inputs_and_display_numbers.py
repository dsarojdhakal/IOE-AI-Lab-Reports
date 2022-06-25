marks = []
nums = 10
def showMarks():
    for i in range(nums):
        number = int(input("Enter a number: "))
        marks.append(number)
    print("The entered 10 marks: ", marks)

showMarks()