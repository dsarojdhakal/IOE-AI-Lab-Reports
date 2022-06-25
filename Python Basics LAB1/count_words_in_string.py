sentence = str(input("Enter a string: \t"))

def wordNumber():
    length = len(sentence.split())
    print("There are ", length, "words in the sentence")

wordNumber()