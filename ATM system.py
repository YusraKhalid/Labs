global total
total = 50000
def withdraw(draw):
	remaining = total - draw
	return remaining

def atm(total):
	print ("Your total amount is:", total)
	draw = input("Enter the amount you want to draw: ")
	try:
		draw = int (draw)
		if draw > 50000:
			raise moreThanTotal

	except:
		print ("Invalid amount.")
		draw = 0

	finally:
		return (draw)


def main():
	pin = "1998"
	pinEntered = input ("Enter the pin: ")
	if pinEntered != pin:
		print("Incorrect pin.")

	else:
		draw = atm(total)
		remaining = withdraw(draw)
		print ("The remaining amount is:", remaining)

	finally:
		print("Transaction complete")
main()
