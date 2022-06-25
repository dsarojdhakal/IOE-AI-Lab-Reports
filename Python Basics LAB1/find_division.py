percentage = int(input("Enter percentage \t"))

def Dvision():
    if percentage > 80 :
        return('Distinction')

    elif percentage > 60 :
        return('First Division')

    elif percentage > 55 :
        return('Second Division')

    elif percentage > 40 :
        return('Third Division')
    else:
        return('Fail')

print(Dvision())
