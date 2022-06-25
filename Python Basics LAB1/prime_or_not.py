def primeNum():
    for num in range(0, 100):
        if num > 1:
            for i in range(2, num):
              if (num%i) == 0:
                 break
            else:
                 print(num, "\t")
print("Prime Numbers between 0 and 100 are : ")
primeNum()