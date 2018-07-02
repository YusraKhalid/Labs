def main():
    listing = []
    num = input("enter a number between 10-100: ")
    try:
        num = int(num)
    except:
        print("invalid input.")
        num = 0
    while (num>= 10) and (num <= 100):

        if not(num in listing):
            listing.append(num)

        num = input("enter a number between 10-100: ")
        try:
            num = int(num)
        except:
            print("invalid input.")
            num = 0
    count = 0

    while count < len(listing):
        print(listing[count])
        count += 1
main()
