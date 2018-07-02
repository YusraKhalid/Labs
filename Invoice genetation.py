def discounted(number,value,special):
	discount = 0.5
	priceOfOne = 1.5
	priceOfMore = 1.5*number
	discountOfMore = 0.5*number
	discountedPrice = priceOfMore - discountOfMore
	if (value == "Y") or (special == "Y"):
		print ("The total was: ",priceOfMore)
		print ("Discount is: ", discountOfMore)
		print ("Discounted price is: ", discountedPrice)

	else:
		print ("The total was: ",priceOfMore)
		print ("Ther is no discount")



def main():
    firstName = input("Enter the customers first name: ")
    lastName = input("Enter the customers last name: ")

    amount = int(input("Enter the number of rentals:"))
    valueDay = input("Is this a value day: ")
    special = input ("Is he a speacial customer: ")

    print(firstName+" "+lastName+ " Rented", amount, "tapes")
    discounted(amount,valueDay,special)
    print ("Thank you for being our customer.")

main()