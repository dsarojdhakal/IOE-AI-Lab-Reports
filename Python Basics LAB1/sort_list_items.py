list1 = [5,4,11,13,51]
n = len(list1)
def sortList():
    for i in range(0, n+1):
        if i + 1 < n:
            if list1[i] > list1[i+1] :
                list1[i], list1[i+1] = list1[i+1], list1[i]

    print(list1[i])

print(sortList())