def main():
    count = 0
    listing= []
    location = 0
    while count < 10:
        elements = input("Enter the element of list: ")
        try:
            elements = int(elements)
        except:
            print("Invalid entery",count+1)
            break

        listing.append(elements)
        if count == 0:
            compare = elements

        if listing[count] > compare:
            compare = listing[count]
            location = count
        count += 1

    print("The largest number is: ",compare)
    print("Its location is: ",location)

main()