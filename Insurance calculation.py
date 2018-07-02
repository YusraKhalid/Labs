def one():
    print("His premium is Rs.4 per thousand.")
    print("His policy amount can not exceed 2 lakh")

def two():
    print("His premium is Rs.3 per thousand.")
    print("His policy amount can not exceed 1 lakh")

def three():
    print("His premium is Rs.6 per thousand.")
    print("His policy amount can not exceed Rs.10,000")

def main():
    health = input("Is person in good health or bad: ")
    age = int(input("Enter age: "))
    residence = input("Does he live in city or village: ")
    gender = input("Is person male or female: ")

    if (health == "good") and (25<age<35) and (residence == "city"):
        print("The person can be insured.")
        if gender == "male":
            one()

        else:
            two()

    elif (health == "bad") and (25<age<35) and (residence == "village") and (gender=="male"):
        print("The person can be insured.")
        three()

    else:
        print("The person can not be insured.")

main()