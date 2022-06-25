myDict = {
    'u':330,
    'v':910,
    'w':880,
    'x':250, 
    'y':500, 
    'z':410
}
print("Dictionary: ", myDict)

def addDict():
    total = 0
    for num in myDict.values():
        total = total + num
    
    print("\nThe Total Sum of Values : ", total)

addDict()