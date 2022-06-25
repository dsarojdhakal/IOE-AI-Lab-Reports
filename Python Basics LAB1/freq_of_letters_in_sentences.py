sentence = str(input("Enter a sentence: "))
Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = len(sentence)

def countFreq():
    for i in range(0,n):
        if sentence.count(Alphabet[i]) > 0 :
            print(Alphabet[i], sentence.count(Alphabet[i]))

        else:
            pass

countFreq()