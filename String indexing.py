def printingOne(a,b,c):
    output = a[b:c]
    return output

def printingTwo(a):
    output = a.upper()
    return output

def three():
    string = "Right now I am doing programming in pyhton."
    print(string)
    indexOne = input("Enter the start of index required in output:  ")
    indexTwo = input("Enter the end of index required in output:  ")
    indexOne = int (indexOne)
    indexTwo = int (indexTwo)
    required1 = printingOne(string,indexOne,indexTwo)
    required2 = printingTwo(required1)
    print(required2)

three()