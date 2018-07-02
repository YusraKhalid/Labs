def reverse(a):
    required1 = a.find(" ")
    if required1:
        reversing1 = a[required1::-1]



    required2 = a.find(" ",required1+1)
    if required2:
        reversing2 = a[required2:required1:-1]


    required3 = a.find(" ",required2+1)
    if required3:
        reversing3 = a[required3:required2:-1]


    required4 = a.find(" ",required3+1)
    if required4:
        reversing4 = a[required4:required3:-1]



    required5 = a.find(" ",required4+1)
    if required5:
        reversing5 = a[required5:required4:-1]


    required6 = a.find(" ",required5+1)
    if required6:
        reversing6 = a[required6:required5:-1]


    required7 = a.find(" ",required6+1)
    if required7:
        reversing7 = a[required7:required6:-1]


    required8 = a.find(" ",required7+1)
    if required8:
        reversing8 = a[required8:required7:-1]


    required9 = a.find(" ",required8+1)
    if required9:
        reversing9 = a[required9:required8:-1]


    required10 = a.find(".",required9+1)
    if required10:
        reversing10 = a[required10:required9:-1]

    if required1 == -1:
        print(reversing1)

    if required2 == -1 and required1 != -1:
        print(reversing1+reversing2)

    if required3 == -1 and required2 != -1:
        print(reversing1+reversing2+reversing3)

    if required4 == -1 and required3 != -1:
        print(reversing1+reversing2+reversing3+reversing4)

    if required5 == -1 and required4 != -1:
        print(reversing1+reversing2+reversing3+reversing4+reversing5)

    if required6 == -1 and required5 != -1:
        print(reversing1+reversing2+reversing3+reversing4+reversing5+reversing6)

    if required7 == -1 and required6 != -1:
        print(reversing1+reversing2+reversing3+reversing4+reversing5+reversing6+reversing7)

    if required8 == -1 and required7 != -1:
        print(reversing1+reversing2+reversing3+reversing4+reversing5+reversing6+reversing7+reversing8)

    if required9 == -1 and required8 != -1:
        print(reversing1+reversing2+reversing3+reversing4+reversing5+reversing6+reversing7+reversing8+reversing9)

    if required10 == -1 and required9 != -1:
        print(reversing1+reversing2+reversing3+reversing4+reversing5+reversing6+reversing7+reversing8+reversing9+reversing10)



def main():
    string = input("Enter a string of not more that 10 words:")
    reverse(string)


main()