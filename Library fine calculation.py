def fiveDays(days):
    fine = 0.5*days
    return fine

def sixToTenDays(days):
    fine = (1*(days-5))+(0.5*5)
    return fine

def tenDays(days):
    fine = (5*(days-10))+(sixToTenDays(10))
    return fine

def main():
    days = int(input("Enter the number of days you are late: "))
    if days<= 5:
        print(fiveDays(days))

    elif (days >5) and (days <=10):
        print(sixToTenDays(days))

    elif (days>10) and (days <= 30):
        print(tenDays(days))

    else:
        print("Membership will be cancelled")

main()